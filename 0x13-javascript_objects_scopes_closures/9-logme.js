#!/usr/bin/node

exports.logMe = function (item) {
    i=0;
    item.forEach(element => {
        console.log(i, ':', element);
        i++;
    });
};
