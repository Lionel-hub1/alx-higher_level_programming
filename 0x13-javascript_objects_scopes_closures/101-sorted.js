#!/usr/bin/node
/**
 * dict - computes a new dictionary based on the initial dictionary
 * newDict: initial dictionary
 * Return: new dictionary
 */

const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  // check if the key is in the object
  if (dict.hasOwnProperty(key)) {
    const value = dict[key];
    if (newDict[value]) {
      // if the key is already in the object push the new key
      newDict[value].push(key);
    } else {
      // Otherwise create a new key with the value
      newDict[value] = [key];
    }
  }
}

console.log(newDict);
