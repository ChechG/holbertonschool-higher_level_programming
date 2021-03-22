#!/usr/bin/node
const num = process.argv[2];
console.log(factorial(num));
function factorial (a) {
  if (a == null) {
    return 1;
  }
  if (a === 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
