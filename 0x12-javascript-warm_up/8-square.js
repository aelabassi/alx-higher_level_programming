#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  const number = Number(size);
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
