#!/usr/bin/node
//
const myVar0 = process.argv[2];
const myVar1 = 'My number: ';
if (isNaN(myVar0)) {
  console.log('Not a number');
} else {
  console.log(myVar1 + myVar0);
}
