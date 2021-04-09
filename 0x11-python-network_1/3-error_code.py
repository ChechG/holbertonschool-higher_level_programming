#!/usr/bin/python3
""" Write a Python script that takes in a URL,
sends a request to the URL and displays the body
f the response (decoded in utf-8). """


import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        urllib.request.urlopen(req)
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
