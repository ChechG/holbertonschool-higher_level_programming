#!/usr/bin/python3
""" check if its instance of inherited class """


def inherits_from(obj, a_class):
    """ check if its instance of inherited class """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
