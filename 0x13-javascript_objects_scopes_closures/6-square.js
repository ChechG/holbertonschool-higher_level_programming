#!/usr/bin/node
const Squareone = require('./5-square');

class Square extends Squareone {
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
