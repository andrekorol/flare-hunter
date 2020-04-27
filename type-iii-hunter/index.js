const Client = require('ftp');

const auth = require('./authentication.json');
const { downloadReportsArchives, extractReports } = require('./reports');

// NOAA's Space Weather Prediction Center FTP server information
const config = {
  host: 'ftp.swpc.noaa.gov',
  user: 'ftp',
  password: auth.email,
};

const ftp = new Client();
const archivesDir = 'events-archives';
const reportsDir = 'events';

downloadReportsArchives(ftp, config, archivesDir).then(() =>
  extractReports(archivesDir, reportsDir)
);
