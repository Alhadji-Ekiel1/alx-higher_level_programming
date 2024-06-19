#!/usr/bin/node

// collects arguments starting from the third one
const args = [];
for (let i = 2; i < process.argv.length; i++) {
  args.push(+process.argv[i]);
}

// Check arguments length
if (args.length < 2) {
  console.log(0);
} else {
  // placement of arguments in descending order
  args.sort((a, b) => b - a);
  // Prints the second biggest number
  console.log(args[1]);
}
