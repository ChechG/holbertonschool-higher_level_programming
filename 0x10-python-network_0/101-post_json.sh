#!/bin/bash
# JSON POST displays the body of the response.
curl -s -X POST -H "Content-type: application/json" -d @$2 $1
