#!/usr/bin/python3
# Function finds peak in list of unsorted ints.


def find_peak(lista):
    """ function finds peak """
    if len(lista) == 0:
        return None
    elif len(lista) == 1:
        return lista[0]
    elif len(lista) == 2:
        return max(lista)
    else:
        mid = int(len(lista) / 2)
        if lista[mid - 1] < lista[mid] > lista[mid + 1]:
            return lista[mid]
        elif lista[mid] < lista[mid - 1]:
            return find_peak(lista[:mid])
        else:
            return find_peak(lista[mid + 1:])
