#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    length = len(str)
    for i in range(0, length):
        if i != n:
            new = new + str[i]
    return new
