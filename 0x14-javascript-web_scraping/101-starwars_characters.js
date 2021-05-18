#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const req = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(req, function (err, res, body) {
  if (err) {
    console.logr(err);
  } else {
    let i;
    let num = 1;
    const personaje = JSON.parse(body).characters.sort();
    const largo = JSON.parse(body).characters.length;
    async function main() {
      for (i = 0; i < largo; i++) {
        const per = 'https://swapi-api.hbtn.io/api/people/' + num + '/';
        if (personaje.includes(per)) {
          request(per, function (error, resp, bdy) {
            if (error) {
              console.log(error);
            } else {
              console.log(JSON.parse(bdy).name);
            }
          });
          num += 1;
        } else {
          num += 1;
          i -= 1;
        }
      }
    }
    main();
  }
});
