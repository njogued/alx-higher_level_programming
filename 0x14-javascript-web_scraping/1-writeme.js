#!/usr/bin/node

// Using the fs module to write to a file
const { writeFile } = require('fs');

// The file as a command line argument
const file = process.argv[2];

// The text is the command line argument 3
const text = process.argv[3];

// Import the file system module
// const fs = require('fs');

writeFile(file, text, 'utf-8', (err) => {
  if (err) throw err;
});
