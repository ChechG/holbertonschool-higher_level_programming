#!/usr/bin/python3
""" Function returns an object represented by a JSON str"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
