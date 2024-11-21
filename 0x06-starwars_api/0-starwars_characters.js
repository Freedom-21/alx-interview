#!/usr/bin/node
/*
 * Script to print all characters of a Star Wars movie in the correct order.
 * The Movie ID is given as the first positional argument.
 * Usage example: ./0-starwars_characters.js 3
 */

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make an API request to get the film details
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie. Status code:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Iterate over character URLs and make requests in sequence
  for (const url of characterUrls) {
    await new Promise((resolve) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          resolve();
          return;
        }

        if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
        resolve();
      });
    });
  }
});
