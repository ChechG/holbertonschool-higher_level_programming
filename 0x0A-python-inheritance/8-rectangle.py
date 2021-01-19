#!/usr/bin/python3
""" New class BaseGeometry based on 7-base_geometry"""


class BaseGeometry():
    """ defining integer validator: type int and > 0 """
    def area(self):
        """ defining area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ defining integer validator and > 0 """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ defining class inherited from BaseGeometry class """
    def __init__(self, width, height):
        """ Instantiation """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
