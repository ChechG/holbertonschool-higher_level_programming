#!/usr/bin/python3
""" New class BaseGeometry based on 9-rectangle"""


class BaseGeometry():
    """ defining integer validator: type int and > 0 """
    def area(self):
        """ defining area method if not defined"""
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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ defining area """
        return self.__width * self.__height

    def __str__(self):
        """ convert to string area """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """ defining class inherited from Rectangle class """
    def __init__(self, size):
        """ Instantiation """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
