#!/usr/bin/node
/**
 * This script prints “My number: ” if the first argument can be converted to an integer
 */
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
