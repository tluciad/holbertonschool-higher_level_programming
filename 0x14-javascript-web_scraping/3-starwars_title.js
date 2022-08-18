#!/usr/bin/node
/* script that prints the title of a Star Wars movie
where the episode number matches a given integer */
const axios = require('axios').default;
const url = process.argv[2];
axios.get('https://swapi-api.hbtn.io/api/films/' + url)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(err => {
    console.log('code: ' + err.response.status);
  });
