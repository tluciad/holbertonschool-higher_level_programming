#!/usr/bin/node
/* s a script that gets the contents of a
webpage and stores it in a file. */
const axios = require('axios').default;
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
axios.get(url)
  .then(response => {
    fs.writeFile(file, response.data, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(err => {
    console.log(err);
  });
