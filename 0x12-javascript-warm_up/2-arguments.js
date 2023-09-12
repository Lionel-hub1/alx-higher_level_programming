#!/usr/bin/node
import { argv } from '2-arguments.js';
/*
 * This script is for printing the message depending on the number of arguments passed to the command
 */<F11>

argv.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});
