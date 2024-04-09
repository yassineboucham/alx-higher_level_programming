#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 2){
    console.log('undefined is undefined');
} else if (argv === 3){
    console.log(argv[2], 'is undefined');
} else {
    console.log(argv[2], argv[3]);
}
