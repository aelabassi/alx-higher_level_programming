#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          printCharacters(characters, 0);
        }
      });
    });
  }
});

const printCharacters = (characters, index) => {
  if (index === characters.length) {
    return;
  }
  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if(index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
};
