#!/usr/bin/python3
"""
1. Divide a matrix
Write a function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
         of integers/floats")
    for x in matrix:
        if not type(x) is list:
            raise TypeError("matrix must be a matrix (list of lists)\
             of integers/floats")
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_m = []
    len1 = len(matrix)
    for i in range(0, len1):
        len2 = len(matrix[i])
        new_l = []
        for j in range(0, len2):
            new_l.append(round(matrix[i][j] / div, 2))
        new_m.append(new_l)
    return new_m
