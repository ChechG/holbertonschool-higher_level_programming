#!/usr/bin/python3
def no_c(my_string):
    new = ""
    c = 'c'
    cM = 'C'
    length = len(my_string)
    for i in range(0, length):
        if my_string[i] == c or my_string[i] == cM:
            continue
        else:
            new = new + my_string[i]
    return new
