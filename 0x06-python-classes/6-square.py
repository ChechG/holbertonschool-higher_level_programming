#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not type(position) is tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not type(position[0]) is int) or (not type(position[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size with value"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """print a square with #"""
        if self.__position[1] is not 0:
            for h in range(0, self.__position[1]):
                print("")
        if self.__size > 0:
            for i in range(0, self.__size):
                if self.position[0] > 0:
                    for k in range(0, self.__position[0]):
                        print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")

    @property
    def position(self):
        """define position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position"""
        self.__position = value
