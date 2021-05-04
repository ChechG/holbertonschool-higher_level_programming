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
    const tareas = JSON.parse(body);
    const largo = tareas.length;
    for (i = 0; i < largo; i++) {
      if (nId === tareas[i].userId) {
        if (!(dict[tareas[i].userId])) {
          dict[tareas[i].userId] = 0;
        }
        dict[tareas[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
