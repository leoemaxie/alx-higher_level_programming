#!/usr/bin/node
const fs = require('fs');
const content = process.argv
  .slice(2, 4)
  .map(file => fs.readFileSync(file, 'utf-8'))
  .join('');

fs.writeFile(process.argv[4], content, err => {
  if (err) {
    console.log('Error copying file');
  }
});
