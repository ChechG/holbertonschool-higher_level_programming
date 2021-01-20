#!/usr/bin/python3
""" append string after a string """


def append_after(filename="", search_string="", new_string=""):
    """ append string after string """
    with open(filename, mode='r') as my_file:
        lines = my_file.readlines()

    with open(filename, mode='w') as my_file:
        for i in lines:
            if search_string in i:
                my_file.write(i + new_string)
            else:
                my_file.write(i)
