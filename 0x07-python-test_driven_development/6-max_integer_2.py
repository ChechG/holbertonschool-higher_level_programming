#!/usr/bin/python3
"""Doc
"""


def max_integer(list=[]):
    """Doc
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1

    # If first element => find another integer
    if list[0] == result and len(list) > 1:
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] != list[0]:
                result = list[i]
                break
            i += 1
    
    return result