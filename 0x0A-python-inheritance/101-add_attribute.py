#!/usr/bin/python3
""" Function to add attribute """


def add_attribute(obj, name, value):
    """ Function to add attribute """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
