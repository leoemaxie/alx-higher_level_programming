#!/usr/bin/node
const size = Number(process.argv[2]);

if (!Number.isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let output = '';

    for (let j = 0; j < size; j++) { output += 'X'; }

    console.log(output);
  }
} else { console.log('Missing size'); }
