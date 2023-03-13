#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let largest = 0;
  for (let x = 2; x < process.argv.length; x++) {
    if (process.argv[x] > largest) {
      largest = process.argv[x];
    }
  }
  console.log(largest);
}
