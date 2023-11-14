#!/usr/bin/node
/**
 * This script is a class Rectangle that defines a rectangle
 * And adds a function of print
 * */

class Rectangle {
  constructor (w, h) {
    // Set the rectangle's width and height only if w and h are greater than 0
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Otherwise, define an empty object
      Object.create(null);
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
