#!/usr/bin/python3
""" New class BaseGeometry based on 7-base_geometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """ defining class inherited from BaseGeometry class """
    def __init__(self, width, height):
        """ Instantiation """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
