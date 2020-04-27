const fs = require('fs');
const tar = require('tar');
const path = require('path');
const { warning, error, success, info } = require('./log-style');

function changeFTPDir(ftpClient, dirPath) {
  // Change the current working directory on a FTP connection
  // and resolve to this new CWD
  return new Promise((resolve, reject) => {
    ftpClient.cwd(dirPath, (err, currentDir) => {
      if (err) reject(err);
      if (currentDir) {
        resolve(currentDir);
      } else {
        ftpClient.pwd((err, cwd) => {
          if (err) reject(err);
          resolve(cwd);
        });
      }
    });
  });
}

exports.downloadReportsArchives = function(
  // Download all the archives of solar events reports from NOAA's
  // FTP server
  ftpClient,
  ftpClientConfig,
  archivesDestDir
) {
  return new Promise((resolve, reject) => {
    if (!fs.existsSync(archivesDestDir)) {
      fs.mkdir(archivesDestDir, err => {
        if (err) reject(err);
        console.log(success(`Created the "${archivesDestDir}" directory`));
      });
    }

    ftpClient.on('error', err => {
      console.log(
        error(
          `${err.name} ${err.code ? ` (${err.code}):` : ':'} ${err.message}`
        )
      );
      ftpClient.end();
    });

    ftpClient.on('greeting', msg => {
      console.log(info(`The server sent: ${msg}`));
    });

    ftpClient.on('close', hadErr => {
      if (hadErr)
        console.log(
          error(
            'The connection to the FTP server has been fully closed due to an error'
          )
        );
      else {
        console.log(
          info('The connection to the FTP server has been fully closed')
        );
        console.log(
          success(`Finished downloading report archives to ${archivesDestDir}`)
        );
      }
      resolve();
    });

    ftpClient.on('end', () => {
      console.log(warning('The connection has ended'));
    });

    ftpClient.on('ready', () => {
      changeFTPDir(ftpClient, 'pub/warehouse').then(cwdPath => {
        console.log(warning(`Changed directory to "${cwdPath}"`));
        ftpClient.list(cwdPath, (err, list) => {
          list
            .filter(entry => entry.type === 'd')
            .forEach(element => {
              const year = element.name;
              const eventsArchive = `${year}_events.tar.gz`;
              ftpClient.get(`${year}/${eventsArchive}`, (err, fileStream) => {
                if (err)
                  console.log(error(`Couldn't download ${eventsArchive}`));
                else {
                  console.log(info(`Downloading ${eventsArchive}...`));
                  fileStream.pipe(
                    fs.createWriteStream(`${archivesDestDir}/${eventsArchive}`)
                  );
                  fileStream.once('close', () => {
                    console.log(success(`Downloaded ${eventsArchive}`));
                    ftpClient.end();
                  });
                }
              });
            });
        });
      });
    });
    ftpClient.connect(ftpClientConfig);
  });
};

function createDestDir(destDir) {
  // Create an empty directory to be used as destination for
  // the decompressed files
  return new Promise(resolve => {
    if (fs.existsSync(destDir)) {
      console.log(
        warning(
          `The '${destDir}' directory already exists under the current working ` +
            'directory\nEverything in it will be deleted/overwritten'
        )
      );
      fs.rmdirSync(destDir, {
        recursive: true,
      });
    }
    fs.mkdirSync(destDir);
    resolve();
  });
}

function extractTxtFiles(archivesDir, destDir) {
  // Extract text files from compressed tarballs
  return new Promise((resolve, reject) => {
    let counter = 0;
    function finishExtraction(tarballPath, numFiles) {
      console.log(info(`Finished extracting reports from ${tarballPath}`));
      counter += 1;
      if (counter === numFiles) {
        console.log(success(`Finished extracting all reports to '${destDir}'`));
        resolve();
      }
    }
    fs.readdir(archivesDir, (err, files) => {
      if (err) reject(err);
      const gzippedTarballs = files.filter(
        file => path.extname(file) === '.gz'
      );
      for (const tarball of gzippedTarballs) {
        const tarballPath = `${archivesDir}/${tarball}`;
        fs.createReadStream(tarballPath)
          .pipe(tar.t())
          .on('entry', entry => {
            if (entry.type === 'File' && path.extname(entry.path) === '.txt') {
              const filename = path.basename(entry.path);
              entry.pipe(fs.createWriteStream(path.join(destDir, filename)));
            }
          })
          .on('end', () => {
            finishExtraction(tarballPath, gzippedTarballs.length);
          });
      }
    });
  });
}

exports.extractReports = function(archivesDir, destDir) {
  // Create a directory and extract all the text files found in the
  // tarballs to it
  return new Promise((resolve, reject) => {
    createDestDir(destDir)
      .then(() => extractTxtFiles(archivesDir, destDir))
      .then(() => resolve())
      .catch(reason => reject(reason));
  });
};
