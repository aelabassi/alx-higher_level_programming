#!/usr/bin/env node
const axios = require('axios');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

axios.get(url)
    .then((response) => {
        const characters = response.data.characters;
        characters.forEach((character) => {
            axios.get(character)
                .then((response) => {
                    console.log(response.data.name);
                })
                .catch((error) => {
                    console.log(error);
                });
        });
    })
    .catch((error) => {
        console.log(error);
    });
