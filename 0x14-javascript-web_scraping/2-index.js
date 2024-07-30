#!/usr/bin/env node
const axios = require('axios');
const fs = require('fs');

const url = process.argv[2];

axios.get(url)
    .then((response) => {
        fs.writeFile(process.argv[3], response.data, 'utf8', (err) => {
            if (err) {
                console.log(err);
            }
        });
    })
    .catch((error) => {
        console.log(error);
    });
