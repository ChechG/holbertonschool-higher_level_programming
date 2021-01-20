#!/usr/bin/python3
"""function that reads a text file and prints it"""


def read_file(filename=""):
    """function that reads a txt file and prints it"""
    with open(filename, mode='r', encoding="utf-8") as myFile:
        print(myFile.read(), end="")
