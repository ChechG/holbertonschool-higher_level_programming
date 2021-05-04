#!/usr/bin/node

const request = require('request');
const webP = process.argv[2];

request(webP, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    let i;
    let nId = 1;
    let num = 0;
    for (i = 0; i < JSON.parse(body).length; i++) {
      if (nId === JSON.parse(body)[i].userId) {
        if (JSON.parse(body)[i].completed === true) {
          num += 1;
          dict[nId] = num;
        }
      } else {
        nId += 1;
        i -= 1;
        num = 0;
      }
    }
    console.log(dict);
  }
});
