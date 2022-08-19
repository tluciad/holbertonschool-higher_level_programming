#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer */
const axios = require('axios').default;
const film = process.argv[2];
axios.get(film)
  .then(response => {
    let num = 0;
    for (const list of response.data.results) {
      for (const element of list.characters) {
        if (element.endsWith('18/')) {
          num++;
          break;
        }
      }
    }
    console.log(num);
  })
  .catch(err => {
    console.log('code: ' + err.response.status);
  });
