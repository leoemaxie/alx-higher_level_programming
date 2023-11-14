#!/usr/bin/node
const numOfOccurence = Number(process.argv[2]);

if (isNaN(numOfOccurence))
{
  console.log('Missing number of occurence');
} else {
  for (let i = 0; i < numOfOccurence; i++) {
      console.log('C is fun');
  }
}
