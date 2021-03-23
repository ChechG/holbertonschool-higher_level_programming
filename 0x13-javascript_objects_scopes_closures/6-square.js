#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super();
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let printR = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        printR += c;
      }
      if (i < this.size - 1) {
        printR += '\n';
      }
    }
    console.log(printR);
  }
}
module.exports = Square;
