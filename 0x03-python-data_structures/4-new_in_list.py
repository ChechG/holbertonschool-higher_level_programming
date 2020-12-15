#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new[idx] = element
        return new
