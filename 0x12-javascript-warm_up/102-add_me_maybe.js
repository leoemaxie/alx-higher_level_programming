#!/usr/bin/node
const addMeMaybe = (x, theFunction) => {
  theFunction(x + 1);
};

module.exports.addMeMaybe = addMeMaybe;
