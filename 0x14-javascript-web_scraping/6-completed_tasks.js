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
    let tareas = JSON.parse(body);
    let largo = tareas.length;
    for (i = 0; i < largo; i++) {
      if (nId === tareas[i].userId) {
        if (tareas[i].completed === true) {
          num += 1;
          dict[tareas[i].userId] = num;
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
