#!/usr/bin/env node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let largest = args[0];
  let sLargest = args[1];

  for (let i = 2; i < args.length; i++) {
    if (args[i] > largest) {
      sLargest = largest;
      largest = args[i];
    } else if (args[i] > sLargest && args[i] !== largest) {
      sLargest = args[i];
    }
  }
  console.log(sLargest);
}
