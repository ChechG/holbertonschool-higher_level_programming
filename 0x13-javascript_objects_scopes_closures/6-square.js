#!/usr/bin/node
const Squareone = require('./5-square');

class Square extends Squareone {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let printR = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        printR += c;
      }
      if (i < this.height - 1) {
        printR += '\n';
      }
    }
    console.log(printR);
  }
}
module.exports = Square;
