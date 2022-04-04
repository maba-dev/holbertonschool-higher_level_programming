#!/usr/bin/node

const args = process.argv;
let x = parseInt(args[2]);
if (Number.isNaN(x)) {
  console.log(1);
} else {
  let result = 1;
  while (x > 0) {
    result = result * x;
    x--;
  }
  console.log(result);
}
