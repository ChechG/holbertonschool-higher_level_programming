#!/usr/bin/python3
""" New class BaseGeometry based on 8-rectangle"""


class BaseGeometry():
    """ defining integer validator: type int and > 0 """
    def area(self):
        """ defining area method if not defiined"""
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

    def area(self):
        """ defining area """
        return self.__width * self.__height

    def __str__(self):
        """ convert to string area """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
