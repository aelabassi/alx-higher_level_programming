#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
