#!/usr/bin/node
const args = process.argv;
if (parseInt(args[2])) {
  const number = parseInt(args[2]);
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
