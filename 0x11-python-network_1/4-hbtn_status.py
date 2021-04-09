#!/usr/bin/python3
""" Write a Python script that fetches given URL """


import requests

if __name__ == "__main__":
    url = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.content.decode('utf-8')))
