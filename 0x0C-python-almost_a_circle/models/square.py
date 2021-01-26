#!/usr/bin/python3
"""Write the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation init"""
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """converts to string"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".format(self.id,
                self.__x, self.__y, self.__width))

    @property
    def size(self):
        """size getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is int:
            if value > 0:
                self.__width = value
                self.__height = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

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

    def update(self, *args, **kwargs):
        """update arguments of Rectangle"""
        my_attr = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, my_attr[i], args[i])
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        new_dict = {'x': self.__x,
                    'y': self.__y,
                    'id': self.id,
                    'size': self.__width}
        return new_dict
