#!/usr/bin/node

const args = process.argv;
const fs = require('fs');
fs.readFile(args[2],
  { encoding: 'utf-8' },
  function (err, data) {
    if (err) { console.log(err); } else { console.log(data); }
  });
