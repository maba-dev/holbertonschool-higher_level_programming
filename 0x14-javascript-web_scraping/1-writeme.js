#!/usr/bin/node
const args = process.argv;
const fs = require('fs')
let data = args[3]
fs.writeFile(args[2], data, (err) => {
      
    // In case of a error throw err.
    if (err) throw err;
    console.log(data);
})