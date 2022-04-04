#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);
if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      if (j < x - 1) {
        process.stdout.write('x');
      } else {
        console.log('x');
      }
    }
  }
}
