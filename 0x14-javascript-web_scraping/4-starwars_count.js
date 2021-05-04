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
    const largo = JSON.parse(body).results;
    for (i = 0; i < largo.length; i++) {
      for (j = 0; j < largo[i].characters.length; j++) {
        n = largo[i].characters[j];
        f = n.includes('/18/');
        if (f === true) {
          num += 1;
        }
      }
    }
    console.log(num);
  }
});
