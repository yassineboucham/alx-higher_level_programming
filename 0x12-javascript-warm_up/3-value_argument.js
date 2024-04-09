#!/usr/bin/node

const { argv } = require('node:process');

let len = 0;

argv.forEach(element => {
    len++;
});

if (len <= 2) {
    console.log('No argument');
} else {
    console.log(argv[2]);
}
