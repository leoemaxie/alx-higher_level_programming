#!/usr/bin/node
const num = Number(process.argv[2]);

if (Number.isNaN(num)) { console.log('Not a Number'); } else { console.log(`number: ${num}`); }
