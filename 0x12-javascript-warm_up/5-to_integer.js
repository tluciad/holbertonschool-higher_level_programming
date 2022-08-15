#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer: */
const myVar0 = process.argv[2];
const myVar1 = 'My number: ';
if (isNaN(myVar0)) {
  console.log('Not a number');
} else {
  console.log(myVar1 + myVar0);
}
