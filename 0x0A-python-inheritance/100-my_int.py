#!/usr/bin/python3
""" Write a class MyInt that inherits from int """


class MyInt(int):
    """Class MyInt"""
    def __eq__(self, num):
        return False

    def __ne__(self, num):
        return True
