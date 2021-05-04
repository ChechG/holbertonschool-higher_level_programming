#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');
const swApi = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(swApi, function (err, res, body) {
  if (err) {
    console.logr(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
