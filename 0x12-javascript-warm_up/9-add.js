#!/usr/bin/node
const arg2 = Number(process.argv[2]);
const arg3 = Number(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(arg2, arg3);
