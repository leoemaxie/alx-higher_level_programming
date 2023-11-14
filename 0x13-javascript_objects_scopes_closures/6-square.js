#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let chars = '';

      for (let j = 0; j < this.size; j++) {
        chars += c ? c : 'X';
      }
      console.log(chars);
    }
  }
}

module.exports = Square;
