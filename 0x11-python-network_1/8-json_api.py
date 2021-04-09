#!/usr/bin/python3
"""Script that takes in a letter and sends a POST
request to given url with the letter as a parameter"""


import requests
from sys import argv

if __name__ == "__main__":
    r = "http://0.0.0.0:5000/search_user"
    url = requests.get(r)

    if len(argv) >= 2:
        url = requests.post(r, data={'q': argv[1]})
    elif len(argv) < 2:
        url = requests.post(r, data={'q': ""})
    try:
        jfile = url.json()
        if jfile:
            print("[{}] {}".format(jfile['id'], jfile['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
