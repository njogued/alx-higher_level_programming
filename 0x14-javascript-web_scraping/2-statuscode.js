#!/usr/bin/node

// Using the request module to make HTTP requests
// request module is deprecated in newer node js versions
// So dont take this too seriously

const address = process.argv[2];

const re = require('request');

re(address, (error, response, body) => {
  if (error) console.log(error);
  process.stdout.write('code: ');
  // console.log("code: ");
  console.log(response.statusCode);
});
