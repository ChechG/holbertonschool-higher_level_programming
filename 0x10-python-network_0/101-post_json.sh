#!/bin/bash
# JSON POST displays the body of the response.
curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d @$2 $1