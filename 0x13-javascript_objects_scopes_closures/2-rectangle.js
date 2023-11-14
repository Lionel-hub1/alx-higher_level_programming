#!/usr/bin/node
// This script is a class Rectangle that defines a rectangle

// A Rectangle must be instantiated with 2 arguments: w and h
class Rectangle {
  constructor (w, h) {
    // Set the rectangle's width and height only if w and h are greater than 0
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Otherwise, define an empty object
      return {};
    }
  }
}

module.exports = Rectangle;
