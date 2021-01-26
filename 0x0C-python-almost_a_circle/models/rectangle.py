#!/usr/bin/python3
"""Write the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation init"""
        super().__init__(id)
        if type(width) is int:
            if width > 0:
                self.__width = width
            elif width <= 0:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")
        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")
        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")
        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle with '#' """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            print(rect)
            return
        for new_l in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            for k in range(0, self.__x):
                rect += " "
            for j in range(0, self.__width):
                rect += "#"
            if i < self.__height - 1:
                rect += "\n"
        print(rect)

    def __str__(self):
        """converts to string"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """update arguments of Rectangle"""
        my_attr = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, my_attr[i], args[i])
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        new_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                    'height': self.__height, 'width': self.__width}
        return new_dict
