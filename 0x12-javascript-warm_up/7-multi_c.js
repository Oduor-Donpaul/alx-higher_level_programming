#!/usr/bin/node
const line = 'C is fun';
const number = process.argv[2];
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log(line);
  }
}
