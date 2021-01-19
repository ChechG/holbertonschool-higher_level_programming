#!/usr/bin/python3
""" New class BaseGeometry based on 5-base_geometry"""


class BaseGeometry():
    """ defining area not implemented """
    def area(self):
        raise Exception("area() is not implemented")
