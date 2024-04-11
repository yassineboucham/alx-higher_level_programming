#!/usr/bin/node
/*
exports.nbOccurences = function (list, searchElement) {
    conter = 0;
    list.forEach(element => {
        if (element === searchElement)  conter++;
    });
    return conter;
};
*/

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
