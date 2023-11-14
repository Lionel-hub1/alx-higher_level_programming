#!/usr/bin/node
/**
 * Square class that inherits from Rectangle class.
 */

// Import the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Definition of the Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the parent class (Rectangle) with the size argument for both width and height
    super(size, size);
  }
}

module.exports = Square;
