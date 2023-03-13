#!/usr/bin/node
const process = require('process');
let num = 0;
process.argv.forEach((val, index) => {
  num += 1;
});
if (num === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
