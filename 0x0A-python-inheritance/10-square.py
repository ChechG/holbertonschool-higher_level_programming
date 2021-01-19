#!/usr/bin/python3
""" New class BaseGeometry based on 9-rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ defining class inherited from Rectangle class """
    def __init__(self, size):
        """ Instantiation """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
