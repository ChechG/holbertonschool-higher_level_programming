#!/usr/bin/python3
"""
2. Say my name
Write a function that prints My name is <first name> <last name>
Prototype: def say_my_name(first_name, last_name=""):
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints a string with two string parameters.
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
