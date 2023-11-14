#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOfOccurence = 0;

  list.forEach(item => item === searchElement ? numOfOccurence++ : '');
  return numOfOccurence;
};
