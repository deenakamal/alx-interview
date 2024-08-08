#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, async (error, response, body) => {
  if (error) {
    console.error(`Error fetching movie data: ${error.message}`);
    return;
  }

  if (response.statusCode === 200) {
    try {
      const movies = JSON.parse(body);
      const characters = movies.characters;

      if (characters.length === 0) {
        console.log('No characters found for this movie.');
        return;
      }

      for (const character of characters) {
        try {
          const characterBody = await fetchCharacterName(character);
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        } catch (error) {
          console.error(`Error fetching character data: ${error.message}`);
        }
      }
    } catch (error) {
      console.error(`Error parsing movie data: ${error.message}`);
    }
  } else {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
  }
});

async function fetchCharacterName(characterEndpoint) {
  return new Promise((resolve, reject) => {
    request.get(characterEndpoint, (error, response, body) => {
      if (error) {
        reject(new Error(`Error fetching character endpoint: ${error.message}`));
      } else if (response.statusCode === 200) {
        resolve(body);
      } else {
        reject(new Error(`Failed to fetch character. Status code: ${response.statusCode}`));
      }
    });
  });
}
