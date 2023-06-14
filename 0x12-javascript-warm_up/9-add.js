#!/usr/bin/node
const process = require('process');
const args = process.argv;

function add (a, b) {
	  const x = a + b;
	  console.log(x);
}

const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

add(num1, num2);
