#!/usr/bin/node
/**
 * This function returns the reversed version of a list
 */

exports.esrever = function (list) {
  // Create a new array to store the reversed elements
  const reversed = [];

  // Iterate over the original array from the end to the beginning
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the new array
    reversed.push(list[i]);
  }

  // Return the reversed array
  return reversed;
};
