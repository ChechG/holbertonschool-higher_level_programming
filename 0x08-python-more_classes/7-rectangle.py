#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by prior ej 6"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        return self.__width * self.__height

    def perimeter(self):
        """definition of perimeter"""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """converts to string"""
        rect = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """returns values"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """deletes rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
