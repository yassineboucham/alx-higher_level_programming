#!/usr/bin/node

const { argv } = require('node:process');

function add(a, b) {
    return a + b;
}

add(Number(argv[2]), Number(argv[3]));
