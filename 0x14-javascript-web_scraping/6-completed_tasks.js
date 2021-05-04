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
        if (tareas[i].completed === true) {
          if (!(tareas[i].userId in dict)) {
            dict[tareas[i].userId] = 0;
          }
          dict[tareas[i].userId] += 1;
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
