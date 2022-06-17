#!/usr/bin/node
const ident = process.argv[2];
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + ident;

function retrived (urlChar) {
  return new Promise(function (resolve, reject) {
    request(urlChar, function getChar (err2, response2, body2) {
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

request(URL, function getList (err, response, body) {
  if (err) {
    throw err;
  } else {
    const urlist = JSON.parse(body).characters;
    getlist(urlist);
  }
});
