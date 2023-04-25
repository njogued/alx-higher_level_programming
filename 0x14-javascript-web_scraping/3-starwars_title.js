#!/usr/bin/node

// Using the request module

const re = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
re(url, (error, response, body) => {
  if (error) throw error;
  const dict = JSON.parse(body);
  console.log(dict.title);
});
