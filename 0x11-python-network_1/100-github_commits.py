#!/usr/bin/python3
"""  Script that takes 2 arguments in order to solve a challenge. """


import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    u = 'https://api.github.com/repos/' + owner + "/" + repo + "/commits"
    url = requests.get(u).json()
    cont = 0
    for key in url:
        if cont < 10:
            print("{}: {}".format(key['sha'], key['commit']['author']['name']))
            cont += 1
        else:
            break
