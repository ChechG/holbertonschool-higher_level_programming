#!/usr/bin/python3
"""Function that writes a str to a txt and returns the num char"""


def write_file(filename="", text=""):
    """Function that writes a str to a txt and returns the num char"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    with open(filename, encoding="utf-8") as myFile:
        return(len(text))
