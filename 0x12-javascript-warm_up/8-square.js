#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  let x = '';
  for (let i = 0; i < (parseInt(process.argv[2])); i++) {
    for (let j = 0; j < (parseInt(process.argv[2])); j++) {
      x += 'X';
    }
    if (i < (parseInt(process.argv[2]) - 1)) {
      x += '\n';
    }
  }
  console.log(x);
}
