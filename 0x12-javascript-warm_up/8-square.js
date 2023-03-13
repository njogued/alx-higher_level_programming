#!/usr/bin/node
const sq = Number(process.argv[2]);
if (isNaN(sq)) {
  console.log('Missing size');
}
for (let i = 0; i < sq; i++) {
  for (let j = 0; j < sq; j++) {
    process.stdout.write('X');
  }
  console.log('');
}
