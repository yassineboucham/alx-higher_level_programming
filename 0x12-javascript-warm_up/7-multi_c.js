#!/usr/bin/node

const { argv } = require('node:process');

if (argv.lenght === 2) {
    console.log('Missing number of occurrences')
} 
for (let i='0'; i<=argv; i++) {
    console.log('C is fun')
}
