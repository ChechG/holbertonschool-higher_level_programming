#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """func that prints sorted list"""
        new_list = list.copy(self)
        new_list.sort()
        print(new_list)
