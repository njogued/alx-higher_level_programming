#!/usr/bin/node
const process = require('process');
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
