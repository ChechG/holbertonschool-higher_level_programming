#!/bin/bash
# JSON POST displays the body of the response.
curl -sH "Content-type: application/json" -X POST -d @$2 $1
