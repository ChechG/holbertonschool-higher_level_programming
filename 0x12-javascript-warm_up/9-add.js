#!/usr/bin/node
console.log(add(process.argv[2], process.argv[3]));
function add (a, b) {
  if (isNaN(parseInt(a)) || isNaN(parseInt(b))) {
    return NaN;
  }
  return parseInt(a) + parseInt(b);
}
