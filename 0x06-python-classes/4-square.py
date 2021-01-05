#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square class"""
    __size = None

    def __init__(self, size=0):
        """__init__"""
        size(size)

    def area(self):
        """area"""
        return self.__size * self.__size

    def size(self):
        """size"""
        return self.__size

    def size(self, value):
        """size with value"""
        if type(size) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")
