#!/usr/bin/node
const times = process.argv[2];
const timesNumber = Number(times);
if (isNaN(timesNumber)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < timesNumber; i++) {
    console.log('C is fun');
  }
}
