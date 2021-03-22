#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No arguments found');
} else if (process.argv.length === 3) {
  console.log('Agument found');
} else if (process.argv.length > 3) {
  console.log('Aguments found');
}
