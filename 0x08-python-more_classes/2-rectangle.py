#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by prior ej 1"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """__init__"""
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    def area(self):
        """definition of area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """definition of perimeter"""
        print("width: {}".format(self.width))
        print("height: {}".format(self.height))
        return (2 * (self.__width + self.__height))
