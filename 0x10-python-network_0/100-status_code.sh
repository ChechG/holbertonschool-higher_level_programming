#!/bin/bash
# Displays only the status code of the response.
curl -so /dev/null -w "%{http-code}" $1
