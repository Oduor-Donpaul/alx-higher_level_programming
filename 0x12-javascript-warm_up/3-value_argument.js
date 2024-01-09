#!/usr/bin/env node

const args = process.argv;

const firstArg = args[2];

if (!firstArg) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
