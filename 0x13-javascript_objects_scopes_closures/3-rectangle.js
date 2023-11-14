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
}

module.exports = Rectangle;
