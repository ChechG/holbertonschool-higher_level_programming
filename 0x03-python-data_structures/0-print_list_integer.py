#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length = len(my_list) - 1
    for i in range(0, length):
        print("{:d}".format(my_list[i]))
