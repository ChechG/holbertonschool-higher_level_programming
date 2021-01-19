#!/usr/bin/python3
""" returns True if the object is exactly an instance, or false """


def is_same_class(obj, a_class):
    """check if its exactly the instance class"""
    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return True
        else:
            return False
