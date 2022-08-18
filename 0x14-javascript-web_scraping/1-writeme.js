#!/usr/bin/node
// a script that writes a string to a file
const fs = require('fs');
const content = process.argv[3];

fs.writeFile(process.argv[2], content, function (err, content) {
  if (err) {
    console.error(err);
  }
});
