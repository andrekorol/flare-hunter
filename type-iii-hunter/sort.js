const jsonfile = require('jsonfile');

const dataFile = 'highIntensityEvents.json';
const sortedDataFile = 'sortedEvents.json';

// Sort the events by frequency range
jsonfile.readFile(dataFile, (err, obj) => {
  if (err) throw err;
  obj.sort(
    (firstEl, secondEl) =>
      parseInt(firstEl['Loc/Frq'].split('-')[1]) -
      parseInt(secondEl['Loc/Frq'].split('-')[1])
  );
  // Reverse the sorted array so that higher frequencies appear first
  obj.reverse();
  jsonfile.writeFile(sortedDataFile, obj, { spaces: 2 }, err => {
    if (err) throw err;
  });
});
