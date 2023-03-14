#!/usr/bin/node
const num = process.argv[2];

if (isNaN(parseInt(num))) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  console.log('X'.repeat(num));
}
