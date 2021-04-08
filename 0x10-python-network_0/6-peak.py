#!/usr/bin/python3
""" Function finds peak in list of unsorted ints """


def find_peak(lista):
    """ function finds peak """
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return lista[0]
    if len(lista) == 2:
        return max(lista)
    mid = int(len(lista) / 2)
    if lista[mid - 1] < lista[mid] and lista[mid] > lista[mid + 1]:
        return lista[mid]
    elif lista[mid] < lista[mid - 1]:
        return find_peak(lista[:mid])
    else:
        return find_peak(lista[mid + 1:])
