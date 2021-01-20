#!/usr/bin/python3
""" Write a class Student based on 9-student """


class Student():
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        """ Student __init__ method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Student to_json method """
        if not attrs:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
