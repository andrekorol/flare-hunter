const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { success, info } = require('./log-style');

function findEventsByType(reportPath, eventType) {
  // Parse a SWPC report text file and return an array of objects
  // of events of a given type
  return new Promise((resolve, reject) => {
    const events = [];
    const readStream = fs.createReadStream(reportPath);
    readStream.on('error', err => {
      reject(err);
    });
    const rl = readline.createInterface({
      input: readStream,
      crlfDelay: Infinity,
    });

    // create a Regular Expression from the given eventType string
    // in order to identify lines containing events of that type
    const eventTypeRegExp = new RegExp(`.*${eventType}.*`);

    rl.on('line', line => {
      if (eventTypeRegExp.test(line)) {
        const event = {};

        // extract the event's date from the path of its report file
        [event.DateStr] = reportPath
          .split(path.sep)
          .slice(-1)[0]
          .match(/[0-9]+/);

        const properties = line.split(/\s+/);

        let counter = 0; // keep track of property position

        // arbitrary event number assigned by SWPC
        event.Event = properties[counter];
        counter += 1;

        // skip optional '+' character after the event number
        if (properties[counter] === '+') {
          counter += 1;
        }

        // The UTC Time (Coordinate Universal Time, same as UT) of the
        // beginning, maximum, and end of the event
        event.Begin = properties[counter];
        counter += 1;
        event.Max = properties[counter];
        counter += 1;
        event.End = properties[counter];
        counter += 1;

        // 3 characters representing the reporting observatory
        // See 'observatories.json' for detailed observatory location
        event.Obs = properties[counter];
        counter += 1;

        // Quality of observation
        event.Q = properties[counter];
        counter += 1;

        // Type of report - see SWPC-README for more information on this
        event.Type = properties[counter];
        counter += 1;

        // Location or frequency, see SWPC-README
        event['Loc/Frq'] = properties[counter];
        counter += 1;

        // Additional information from the report, chosen
        // on the basis of the report type
        event.Particulars = properties[counter];
        counter += 1;

        // The SWPC-assigned solar region number
        event['Reg#'] = properties[counter];

        events.push(event);
      }
    });
    rl.on('close', () => {
      resolve(events);
    });
  });
}

exports.parseReports = function(reportsDir, destJSONFile, eventType) {
  return new Promise((resolve, reject) => {
    console.log(
      info(
        `Started extracting type ${eventType} events from the report files` +
          ` on '${reportsDir}'`
      )
    );
    fs.readdir(reportsDir, (err, files) => {
      if (err) reject(err);
      const findPromisses = files.map(filename => {
        const filePath = path.join(reportsDir, filename);
        return findEventsByType(filePath, 'III');
      });
      Promise.all(findPromisses)
        .then(reportEvents => {
          console.log(success(`Finished extracting type ${eventType} events`));
          const eventsArray = [];
          for (const events of reportEvents) {
            if (events.length !== 0) {
              for (const event of events) {
                eventsArray.push(event);
              }
            }
          }
          console.log(
            info(
              `Started writing type ${eventType} events to '${destJSONFile}'`
            )
          );
          fs.writeFile(
            destJSONFile,
            JSON.stringify(eventsArray, null, 2),
            'utf-8',
            err => {
              if (err) reject(err);
              console.log(success(`Finished writing to '${destJSONFile}'`));
              resolve();
            }
          );
        })
        .catch(reason => reject(reason));
    });
  });
};
