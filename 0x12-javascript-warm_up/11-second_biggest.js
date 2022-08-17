#!/usr/bin/node
// searches the second biggest integer in the list of arguments
const big = 0;
const args = process.argv.slice(2);
function SecondBiggest (big, args) {
  if (process.argv.length <= 3) {
    return (0);
  } else if (args.length > 1) {
    args.sort();
    big = args[args.length - 2];
  }
  return (big);
}
console.log(SecondBiggest(big, args));
