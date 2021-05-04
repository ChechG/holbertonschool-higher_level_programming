#!/usr/bin/node

const request = require('request');
const swApi = process.argv[2];
request(swApi, function (err, res, body) {
  if (err) {
    console.logr(err);
  } else {
    let i;
    let j;
    let n;
    let f;
    let num = 0;
    for (i = 0; i < 7; i++) {
      const largo = JSON.parse(body).results[i].characters;
      for (j = 0; j < largo.length; j++) {
        n = JSON.parse(body).results[i].characters[j];
        f = n.includes('18');
        if (f === true) {
          num += 1;
        }
      }
    }
    console.log(num);
  }
});
