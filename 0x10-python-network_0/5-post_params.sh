#!/bin/bash
# sends POST request to URL, and displays body of response
curl $1 -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
