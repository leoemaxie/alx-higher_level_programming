#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let chars = '';

      for (let j = 0; j < this.size; j++) {
        chars += c || 'X';
      }
      console.log(chars);
    }
  }
}

module.exports = Square;
