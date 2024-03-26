#!/usr/bin/env node

const request = require('request');

const url = process.argv[2];

const characterId = 18;

let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode!= 200) {
    console.error(response.statusCode)
    return;
  }
  const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
});
