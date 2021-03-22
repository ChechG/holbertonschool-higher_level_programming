#!/usr/bin/node
if (parseInt(process.argv[2]) >= 0) {
  console.log('Number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
