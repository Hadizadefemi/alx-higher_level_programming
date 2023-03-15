#!/usr/bin/node

let argv = process.argv;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  argv = argv.slice(2);
  const sortedArr = argv.sort((a, b) => a - b);
  console.log(sortedArr[argv.length - 2]);
}
