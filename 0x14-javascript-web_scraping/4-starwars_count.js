#!/usr/bin/node

const args = process.argv;
const axios = require('axios').default;
axios
  .get(`${args[2]}`)
  .then((response) => {
    let i = 0;
    for (const film of response.data.results) {
      for (const listActors of film.characters) {
        if (listActors.includes('people/18/')) {
          i++;
        }
      }
    }
    console.log(i);
  })
  .catch((err) => {
    console.error(err);
  });
