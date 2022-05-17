#!/usr/bin/node

const args = process.argv;
const axios = require('axios').default;
const fs = require('fs');
axios
  .get(args[2])
  .then((response) => {
    if (response.status === 200) {
      fs.writeFile(`./${args[3]}`, response.data, { flag: 'w+' }, (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  })
  .catch((err) => {
    console.error(err);
  });
