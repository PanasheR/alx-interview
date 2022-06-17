#!/usr/bin/node
const ind = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + ind;
const requested = require('request');

function retrived (charUrl) {
  return new Promise(function (resolve, reject) {
    requested(charUrl, function getChar (err2, response2, body2) {
      if (err2) {
        reject(err2);
      } else {
        resolve(JSON.parse(body2).name);
      }
    });
  });
}

async function getlist (urlist) {
  for (const urlChar of urlist) {
    const character = await retrived(urlChar);
    console.log(character);
  }
}

requested(url, function getList (err, response, body) {
  if (err) {
    throw err;
  } else {
    const urlist = JSON.parse(body).characters;
    getlist(urlist);
  }
});
