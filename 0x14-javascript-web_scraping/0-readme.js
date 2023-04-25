#!/usr/bin/node

// Using the fs module to read and display the contents of a file

// Get the file name => Command line argument 2
const file = process.argv[2];

// import the file system module(fs)
const fs = require('fs');

// Read the file using fs.readFile
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(data);
    return;
  }
  console.log(data);
});
