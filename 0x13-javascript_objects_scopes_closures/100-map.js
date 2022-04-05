#!/usr/bin/node

const list = require('./100-data').list;

let i = 0;
console.log(list);
const Map = list.map(x => x * i++);
console.log(Map);
