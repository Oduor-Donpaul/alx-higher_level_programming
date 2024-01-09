#!/usr/bin/env node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const args = process.argv;
const argOne = parseInt(args[2]);
const argTwo = parseInt(args[3]);

add(argOne, argTwo);
