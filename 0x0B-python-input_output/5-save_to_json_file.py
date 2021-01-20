#!/usr/bin/python3
""" Function writes an Obj to a txt, using a JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """ Function writes an Obj to a txt, using a JSON rep"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
