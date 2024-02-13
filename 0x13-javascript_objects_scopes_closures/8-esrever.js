#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];

  list.forEach(item => rev.unshift(item));
  return rev;
};
