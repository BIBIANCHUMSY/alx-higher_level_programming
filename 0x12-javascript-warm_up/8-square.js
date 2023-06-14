#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (isNaN(args[2])) {
	  console.log('Missing size');
} else {
	  const x = parseInt(args[2]);

	  for (let i = 0; i < x; i++) {
		      let j = 0;
		      let row = '';
		      while (j < x) {
			            row = row + 'X';
			            j++;
			          }
		      console.log(row);
		    }
}
