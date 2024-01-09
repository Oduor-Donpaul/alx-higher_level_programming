#!/usr/bin/env node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  const arg = parseInt(args[2]);
  console.log(`My number: ${arg}`);
}
