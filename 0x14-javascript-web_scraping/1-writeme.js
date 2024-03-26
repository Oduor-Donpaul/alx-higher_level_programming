#!/usr/bin/env node

const fs = require('fs');

const filePath = process.argv[2];

const dataToWrite = process.argv[3];

fs.writeFile(filePath, dataToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
})
