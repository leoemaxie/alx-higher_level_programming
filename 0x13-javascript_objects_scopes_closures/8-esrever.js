#!/usr/bin/node
exports.esrever = function (list) {
  let rev = [];

  list.forEach(item => rev.unshift(item));
  return rev;
};
