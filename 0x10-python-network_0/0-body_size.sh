#!/bin/bash
# script that takes URL, sends request to it, displays size of body response
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
