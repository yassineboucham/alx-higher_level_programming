#!/usr/bin/node

const { argv } = require('node:process');

if (!Number(argv[2])) {
    console.log('Missing number of occurrences');
} else if (Number(argv[2]) > 0) {
    for (let i=0; i<Number(argv[2]); i++) {
        console.log('C is fun');
    }
}
