#!/usr/bin/node
/**
 * logMe - prints the number of arguments already printed and the new argument
 */
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
