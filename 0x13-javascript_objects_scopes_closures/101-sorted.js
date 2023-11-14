#!/usr/bin/node
const dict = require('./101-data').dict;
const ids = new Set(Object.values(dict));
const sortedIds = Array.from(ids).sort((a, b) => a - b);
const newDict = Object.fromEntries(sortedIds.map(value => [value, []]));

Object.entries(dict).forEach(([key, value]) => newDict[value].push(key));
console.log(newDict);
