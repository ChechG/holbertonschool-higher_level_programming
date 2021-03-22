#!/usr/bin/node
const nums = process.argv.slice(2);
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  nums.sort();
  console.log(nums[nums.length - 2]);
}
