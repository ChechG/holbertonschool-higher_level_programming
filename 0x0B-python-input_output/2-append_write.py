#!/usr/bin/python3
"""Function appends a str to txt and returns num of char added"""


def append_write(filename="", text=""):
    """Function appends a str to txt and returns num of char added"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
    with open(filename, encoding="utf-8") as myFile:
        return(len(text))
