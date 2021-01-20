#!/usr/bin/python3
""" Function that returns the dict description with simple data structure """
MyClass = __import__('8-my_class').MyClass


def class_to_json(obj):
    return obj.__dict__
