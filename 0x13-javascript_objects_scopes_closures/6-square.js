#!/usr/bin/node

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }

    charPrint(c) {
        if (c === undefined) {
            this.print();
        } else {
            for (let i=0; i<size; i++) {
                console.log(c.repeat(size));
            }
        }
    }
};
