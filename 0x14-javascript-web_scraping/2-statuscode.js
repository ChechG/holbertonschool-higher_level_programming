#!/usr/bin/node

const req = process.argv[2];
const request = require('request');

request(req, function(err, res, body) {
    console.log("code: " + res.statusCode);
});
