#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w * h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let chars = '';

      for (let j = 0; j < this.width; j++) {
        chars += 'X';
      }
      console.log(chars);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
