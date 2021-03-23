#!/usr/bin/node
exports.converter = function (base) {
  function p4ja (esto) {
    return esto.toString(base);
  }
  return p4ja;
};
