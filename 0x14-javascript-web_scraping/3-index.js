#!/usr/bin/env node
const axios = require('axios');

const url = process.argv[2];

axios.get(url)
    .then((response) => {
        // only users that completed the task
        const completed_tasks = response.data.filter((task) => task.completed === true);
        const completed = {};
        completed_tasks.forEach((task) => {
            if (completed[task.userId] === undefined) {
                completed[task.userId] = 1;
            } else {
                completed[task.userId] += 1;
            }
        }
        );
        console.log(completed);
    })
    .catch((error) => {
        console.log(error);
    });
