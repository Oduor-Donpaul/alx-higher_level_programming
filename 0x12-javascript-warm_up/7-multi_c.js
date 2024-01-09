#!/usr/bin/node

const args = process.argv;

const x = args[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  const xInt = parseInt(x);
  for (let i = 0; i < xInt; i++) {
    console.log('C is fun');
  }
}
