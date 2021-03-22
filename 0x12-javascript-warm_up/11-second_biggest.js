#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  const nums = process.argv.slice(2);
  const arrnums = [];
  for (let i = 0; i < nums.length; i++) {
    arrnums.push(parseInt(nums[i]));
  }
  arrnums.sort(function (a, b) { return a - b; });
  console.log(arrnums[arrnums.length - 2]);
}
