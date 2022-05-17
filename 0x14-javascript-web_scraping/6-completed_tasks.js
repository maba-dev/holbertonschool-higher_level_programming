#!/usr/bin/node

const args = process.argv;
const axios = require('axios').default;

const List = {};
let value;
axios
  .get(args[2])
  .then((response) => {
    for ([, value] of Object.entries(response.data)) {
      if (value.completed === true) {
        if (List[value.userId] === undefined) {
          List[value.userId] = 0;
        }
        List[value.userId] += 1;
      }
    }
    console.log(List);
  })
  .catch((err) => {
    console.error(err);
  });
