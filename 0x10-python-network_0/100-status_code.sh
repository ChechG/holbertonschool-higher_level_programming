#!/bin/bash
# Displays only the status code of the response.
curl -o /dev/null -sw "%{http-code}" $1
