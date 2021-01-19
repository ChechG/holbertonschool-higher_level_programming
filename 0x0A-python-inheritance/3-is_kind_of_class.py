#!/usr/bin/python3
""" function that returns True if the object is exactly an instance,
or false """


def is_kind_of_class(obj, a_class):
    """ checks if obj is kind of a_class instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
