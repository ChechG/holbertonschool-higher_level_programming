#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=0):

            size(size)

    def area(self):
        return self.__size * self.__size

    def size(self):
        return self.__size
        
    def size(self, value):
        if type(size) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")

    
