#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    conter = 0;
    list.forEach(element => {
        if (element === searchElement)  conter++;
    });
    return conter;
};
