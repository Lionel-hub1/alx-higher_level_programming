#!/usr/bin/node
/**
 * newList - computes a new list based on the initial list
 * @list: initial list
 * Return: new list
 */

const list = require('./100-data').list;

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
