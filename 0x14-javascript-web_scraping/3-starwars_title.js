#!/usr/bin/node

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const request = require('request');

request.get(url, (error, response, body) => {
  if (error) {
    console.error("Error:", error);
  }
  if (response.statusCode != 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }
  try {
    const movieData = JSON.parse(body);
    console.log(movieData.title)
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});
