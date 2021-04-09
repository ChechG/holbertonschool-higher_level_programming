#!/usr/bin/python3
"""  script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id """


import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    u = 'https://api.github.com/user'
    url = requests.get(u, auth=HTTPBasicAuth(username, token))
    if url.status_code == 200:
        dic = url.json()
        print(dic['id'])
    else:
        print("None")
