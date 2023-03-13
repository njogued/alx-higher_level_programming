#!/usr/bin/node
const arg2 = Math.trunc(process.argv[2]);
function fact (x) {
  if (isNaN(arg2)) {
    return 1;
  } else {
    if (x === 1) {
      return 1;
    }
    return (x * fact(x - 1));
  }
}
console.log(fact(arg2));
