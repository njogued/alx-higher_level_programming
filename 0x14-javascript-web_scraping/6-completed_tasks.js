#!/usr/bin/node

// Print the number of completed tasks

const address = process.argv[2];

const rq = require('request');
let tasks = 0;

// Declare a dict that will be updated with tasks and id values
const dict = {};

rq(address, (error, response, body) => {
  if (error) throw error;
  const output = JSON.parse(body);
  for (let i = 1; i <= 10; i++) {
    tasks = 0;
    for (let j = 0; j <= output.length; j++) {
      // output[j] prevents running out of index
      if (output[j] && output[j].userId === i && output[j].completed === true) { tasks += 1; }
    }
    if (tasks) dict[i] = tasks;
    // console.log(`'${i}': ${tasks}`)
  }
  console.log(dict);
});
