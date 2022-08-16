#!/usr/bin/node
// a script that prints x times “C is fun”
const x = process.argv[2];
let i;
if (isNaN(x)) {
    console.log('Missing size');
}
for (i = 0; i < x; i++) {
    console.log('X'.repeat(x));
}
