#!/usr/bin/python3
""" New class BaseGeometry based on 6-base_geometry"""


class BaseGeometry():
    """ defining integer validator: type int and > 0 """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
