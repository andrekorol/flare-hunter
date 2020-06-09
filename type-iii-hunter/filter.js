const jsonfile = require('jsonfile');

// Filter only Type III events with an intensity value of 3
const dataFile = 'typeIIIEvents.json';
const filteredData = [];
const filteredDataFile = 'highIntensityEvents.json';

jsonfile.readFile(dataFile, (err, obj) => {
  if (err) throw err;
  for (const event of obj) {
    if (event.Particulars.split('/')[1] === '3') filteredData.push(event);
  }
  jsonfile.writeFile(filteredDataFile, filteredData, { spaces: 2 }, err => {
    if (err) throw err;
  });
});
