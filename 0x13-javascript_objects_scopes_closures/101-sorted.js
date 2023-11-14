#!/usr/bin/node
/**
 * dict - computes a new dictionary based on the initial dictionary
 * newDict: initial dictionary
 * Return: new dictionary
 */

const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}

console.log(newDict);
