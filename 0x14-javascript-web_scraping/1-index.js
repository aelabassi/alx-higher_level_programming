#!/usr/bin/env node
const axios = require('axios');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

axios.get(url)
     .then((response) => {
       const films = response.data;
       console.log(films.title);
     })
    .catch((error) => {
          console.error(error);
        });