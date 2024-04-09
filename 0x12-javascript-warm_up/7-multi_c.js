#!/usr/bin/node

const { argv } = require('node:process');

if (argv.lenght === 2) {
    console.log('Missing number of occurrences');
} else if (argv[2] > '0') {
    for (let i='0'; i<=argv[2]; i++) {
        console.log('C is fun');
    }
}
