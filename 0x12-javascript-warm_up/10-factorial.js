#!/usr/bin/env node

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  } else {
    const result = n * factorial(n - 1);
    return result;
  }
}

const argument = process.argv[2];

const N = parseInt(argument);

const myResult = factorial(N);

console.log(myResult);
