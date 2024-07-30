#!/usr/bin/env node
const axios = require('axios');
const url = process.argv[2];
// url = 'https://swapi-api.hbtn.io/api/films/';
axios.get(url)
      .then((response) => {
        let count = 0;
        console.log(response.data)
        for (const film of response.data.results) {
          for (const character of film.characters) {
            if (character.endsWith('/18/')) {
              count++;
            }
          }
        }
        console.log(count);
      })
        .catch((error) => {
            console.error(error);
        });