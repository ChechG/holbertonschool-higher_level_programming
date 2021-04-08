#!/bin/bash
# sends GET request to URL, displays body of response
curl $1 -sX GET -H "X-HolbertonSchool-User-Id: 98"
