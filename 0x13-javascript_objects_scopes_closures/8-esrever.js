#!/usr/bin/node
/*
exports.esrever = function (list) {
    let newlist = [];
        for (let i = list.length - 1; i >= 0; i--) {
            newlist.push(list[i]);
        }
    return newlist;
};
*/

exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
