#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

const data = args[3];
fs.writeFile(args[2], data, (err) => {
  if (err) { throw err; } else { console.log(data); }
});
