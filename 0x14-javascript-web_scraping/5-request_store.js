#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const webP = process.argv[2];
const filename = process.argv[3];

request(webP, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
