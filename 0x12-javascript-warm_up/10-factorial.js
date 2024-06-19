#!/usr/bin/node
// here we compute factorial recursively
function computeFactorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * computeFactorial(n - 1);
}

// convert first argument to a number from the command line
const arg = +process.argv[2];

// Compute and print the factorial
console.log(computeFactorial(arg));
