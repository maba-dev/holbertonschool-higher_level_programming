#!/usr/bin/node

exports.esrever = function (list) {
  const size = list.length;
  let tmp;
  let j = size - 1;
  for (let i = 0; i < (size / 2); i++) {
    tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    j = j - 1;
  }
  return list;
};
