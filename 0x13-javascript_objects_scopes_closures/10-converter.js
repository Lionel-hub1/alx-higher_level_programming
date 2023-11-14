#!/usr/bin/node
/**
 * converter - converts a number from base 10 to another base passed as argument
 * @base: base to convert to
 * @num: number to convert
 * Return: converted number
 */

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
