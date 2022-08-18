#!/usr/bin/node
// function that returns the reversed version of a list:
exports.esrever = function (list) {
  const revArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revArray.push(list[i]);
  }
  return revArray;
};
