#!/usr/bin/python3
# Function finds peak in list of unsorted ints.


def find_peak(list_of_integers):
    """ function finds peak """
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    else:
        for i in range(1, len(list_of_integers)):
            if list_of_integers[i] > list_of_integers[i - 1] \
               and list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
            elif i == len(list_of_integers) - 1:
                return list_of_integers[i]
