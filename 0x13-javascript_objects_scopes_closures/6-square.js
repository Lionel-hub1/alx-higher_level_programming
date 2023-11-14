#!/usr/bin/node
/**
 * Class Square that defines a square and inherits from Square of 5-square.js
 */

class Square extends require('./5-square') {
  // Method that prints the rectangle using the character c
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
