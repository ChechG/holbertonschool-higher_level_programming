#!/usr/bin/node

const request = require('request');
const webP = process.argv[2];

request(webP, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    let i;
    const tareas = JSON.parse(body);
    for (i = 0; i < tareas.length; i++) {
      if (tareas[i].completed === true) {
        if (!(dict[tareas[i].userId])) {
          dict[JSON.parse(body)[i].userId] = 0;
        }
        dict[JSON.parse(body)[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
