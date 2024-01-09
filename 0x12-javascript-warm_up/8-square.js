#!/usr/bin/env node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  const xInt = parseInt(args[2]);
  for (let i = 0; i < xInt; i++) {
    let row = '';
    for (let j = 0; j < xInt; j++) {
      row += '* ';
    }
    console.log(row);
  }
}
