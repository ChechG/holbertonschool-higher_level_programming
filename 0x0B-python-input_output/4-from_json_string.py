#!/usr/bin/python3
""" Function returns an object represented by a JSON str"""
import json


def from_json_string(my_str):
    """ Function returns an object represented by a JSON str"""
    return json.loads(my_str)
