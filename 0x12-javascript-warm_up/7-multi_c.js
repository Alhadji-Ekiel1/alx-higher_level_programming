#!/usr/bin/node
const x = +process.argv[2];

if (!x || x < 1) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
