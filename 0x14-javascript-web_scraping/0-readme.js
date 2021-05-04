#!/usr/bin/node

const arg1 = process.argv[2];
const fs = require('fs');

fs.readFile(arg1, 'utf8' , (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
})
