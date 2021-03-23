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
