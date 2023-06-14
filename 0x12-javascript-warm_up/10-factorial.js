#!/usr/bin/node
const process = require('process');
const args = process.argv;

function factorial (n) {
	  if (isNaN(n) || n < 2) return 1;
	  else return n * factorial(n - 1);
}
const num = parseInt(args[2]);
const result = factorial(num);

console.log(result);
