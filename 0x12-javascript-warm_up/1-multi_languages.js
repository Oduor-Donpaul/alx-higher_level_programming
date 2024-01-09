#!/usr/bin/node

const lines = {
  line_one: 'C is fun',
  line_two: 'Python is cool',
  line_three: 'JavaScript is amazing'
};

const myLines = Object.values(lines);

myLines.forEach(line => {
  console.log(line);
});
