const fs = require('fs');
const path = require('path');
const csv = require('fast-csv');
const moment = require('moment');
require('twix');

const RAW_DIR = 'raw';
const DIST_DIR = 'dist';
const LABEL_DURATION = 'week';
const LABEL_PSA = 'PSA';
const LABEL_OFFENSE = 'OFFENSE';
// const LABEL_DATE = 'REPORT_DAT';
const LABEL_DATE = 'REPORT_DATE';
const CRIMES = ['BURGLARY',
  'THEFT/OTHER',
  'THEFT F/AUTO',
  'MOTOR VEHICLE THEFT',
  'ROBBERY',
  'ASSAULT W/DANGEROUS WEAPON',
  'SEX ABUSE',
  'HOMICIDE',
  'ARSON'
  ];

// const DATE_FORMAT = 'M/D/YYYY hh:mm:ss A';
const DATE_FORMAT = 'YYYY-MM-DD HH:mm:ss';

if (!fs.existsSync(DIST_DIR)) {
  fs.mkdirSync(DIST_DIR);
}

var files = fs.readdirSync(RAW_DIR);

files.forEach((file) => {
  if (file.endsWith('.csv')) {
    processFile(file);
  }
});

function processFile(file) {
  console.log(file);
  var processed = {};
  var startDate = null;
  for (var i = 0; i < CRIMES.length; i++) {
    processed[CRIMES[i]] = [];
  }
  csv.fromPath(path.join(RAW_DIR, file), { headers: true })
    .on('data', function(data) {
      var info = extractInfo(data);
      if (startDate === null) {
        startDate = info.date;
      }
      info[LABEL_DURATION] = getDuration(info.date, startDate);
      addInfo(info, processed);
    })
    .on('end', function() {
      console.log('read done');
      writeToFile(processed, file);
    });
}

function getDuration(date, startDate) {
  var t = moment(startDate).twix(date);
  return Math.ceil(t.count('days') / 7);
}

function addInfo(info, processed, startDate) {
  var isNew = true;
  if (!has(processed, info.type)) {
    console.log('new type:');
    console.log(info.type);
    return;
  }
  for (var i = 0; i < processed[info.type].length; i++) {
    if (doesLabelExist(info, processed, i)) {
      processed[info.type][i][info.type]++;
      isNew = false;
      break;
    }
  }
  if (isNew) {
    var newObj = {};
    newObj[LABEL_DURATION] = info[LABEL_DURATION];
    newObj[LABEL_PSA] = info[LABEL_PSA];
    newObj[info.type] = 1;
    processed[info.type].push(newObj);
  }
}

function has(object, key) {
  return object ? hasOwnProperty.call(object, key) : false;
}

function doesLabelExist(info, processed, i) {
  return processed[info.type][i][LABEL_DURATION] === info[LABEL_DURATION] &&
    processed[info.type][i][LABEL_PSA] === info[LABEL_PSA];
}

function extractInfo(row) {
  // console.log(row[LABEL_OFFENSE]);
  // console.log(row[LABEL_DATE]);
  // console.log(moment(row[LABEL_DATE], 'M/D/YYYY hh:mm:ss A').format());
  var info = {
    date: moment(row[LABEL_DATE], DATE_FORMAT),
    type: row[LABEL_OFFENSE]
  };
  info[LABEL_PSA] = +row[LABEL_PSA];
  return info;
}

function writeToFile(data, file) {
  for (var property in data) {
    if (data.hasOwnProperty(property) && data[property].length > 0) {
      writeCrimeType(property, file, data);
    }
  }
}

function writeCrimeType(type, file, data) {
  data[type].sort(sortByDuration);
  normalizeDurationStart(data[type]);
  csv.writeToPath(path.join(DIST_DIR, getSafeFileName(file + '_' + type) + '.csv'), data[type], { headers: true })
  .on('finish', function() {
    console.log(type + ' write done!');
  });
}

function normalizeDurationStart(data) {
  var offset = -data[0][LABEL_DURATION];
  for (var i = 0; i < data.length; i++) {
    data[i][LABEL_DURATION] += offset + 1;
  }
}

function sortByDuration(a, b) {
  if (a[LABEL_DURATION] < b[LABEL_DURATION]) {
    return -1;
  }
  if (a[LABEL_DURATION] > b[LABEL_DURATION]) {
    return 1;
  }
  return sortByPSA(a, b);
}

function sortByPSA(a, b) {
  if (a[LABEL_PSA] < b[LABEL_PSA]) {
    return -1;
  }
  if (a[LABEL_PSA] > b[LABEL_PSA]) {
    return 1;
  }
  return 0;
}

function getSafeFileName(s) {
  return s.replace(/[^a-z0-9.]/gi, '_');
}
