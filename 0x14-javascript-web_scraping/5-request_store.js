#!/usr/bin/node

// Script takes in the url and stores the contents
// in a file

const address = process.argv[2];
// The file to store output in
const file = process.argv[3];
// Import require
const fs = require('fs');
const rq = require('request');

rq(address, (error, response, body) => {
  if (error) throw error;
  fs.writeFile(file, body, 'utf-8', (error) => {
  if (error) console.log(error)
  });
  });
