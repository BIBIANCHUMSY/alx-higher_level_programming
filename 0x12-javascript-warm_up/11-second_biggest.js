#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length <= 3) {
	  console.log(0);
} else {
	  args.sort(function (a, b) { return b - a; });
	  const secBiggest = args[3];
	  console.log(secBiggest);
}
