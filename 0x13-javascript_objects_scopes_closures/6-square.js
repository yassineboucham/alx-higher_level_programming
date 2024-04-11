#!/usr/bin/node

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }

    charPrint(c) {
        if (c === undefined) {
            for (let i=0; i<size; i++) {
                console.log('X'.repeat(size));
            }
        } else {
            for (let i=0; i<size; i++) {
                console.log(c.repeat(size));
            }
        }
    }
};
