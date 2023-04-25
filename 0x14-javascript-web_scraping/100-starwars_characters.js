#!/usr/bin/node

// Use the starwars api to list characters in films

const film = process.argv[2];
const film_url = 'https://swapi-api.alx-tools.com/api/films/' + film;
const rq = require('request');


rq(film_url, (error, response, body) => {
  if (error) throw error;
  const output = JSON.parse(body);
  //console.log(output.characters)
  for (let i = 0; i <= output.characters.length; i++) {
    if (output.characters[i]) {
    rq(output.characters[i], (err, resp, bod) => {
      if (err) throw err;
      const character = JSON.parse(bod);
      console.log(character.name)
    });
    }
    }
})
