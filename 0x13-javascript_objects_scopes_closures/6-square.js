#!/usr/bin/node

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }

    charPrint(c) {
        if (c) {
            for (i=0; i<size; i++) {
                console.log(c.repeat(size));
            }
        } else {
            for (i=0; i<size; i++) {
                console.log('X'.repeat(size));
            }
        }
    }
};
