#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
fs.readFile(args[2],
  { encoding: 'utf-8' },
  function (err, data) {
    if (data) { console.log(data); } else { console.log(err); }
  });
