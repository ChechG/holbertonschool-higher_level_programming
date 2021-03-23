#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      if (i < this.height - 1) {
        rect += '\n';
      }
    }
    console.log(rect);
  }

  rotate () {
    const curr = this.height;
    this.height = this.width;
    this.width = curr;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;

const Squareone = require('./5-square');

class Square extends Squareone {
  constructor (size) {
    super();
    this.size = size;
  }

  charPrint (c) {
    if (c == null) {
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
