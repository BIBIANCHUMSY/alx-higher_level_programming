#!/usr/bin/node
const process = require('process');
const args = process.argv;
let arg1 = args[2];
let arg2 = args[3];

if (!args[2]) {
	  arg1 = 'undefined';
	  arg2 = 'undefined';
} else if (!args[3]) {
	  arg1 = args[2];
	  arg2 = 'undefined';
} else {
	  arg1 = args[2];
	  arg2 = args[3];
}

console.log(arg1 + ' is ' + arg2);
