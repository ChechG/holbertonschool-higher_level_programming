#!/usr/bin/python3
"""
6. Matrix multiplication
Write a function that multiplies 2 matrices:
Prototype: def matrix_mul(m_a, m_b):
"""


def matrix_mul(m_a, m_b):
    """
    Write a function that multiplies 2 matrices:
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    lenA = 0
    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
        lenA = len(x)
    lenB = 0
    for y in m_b:
        if type(y) is not list:
            raise TypeError("m_b must be a list of lists")
        lenB = len(y)
    if not m_a:
        raise ValueError("m_a can't be empty")
    for elem in m_a:
        if not elem:
            raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for eleme in m_b:
        if not eleme:
            raise ValueError("m_b can't be empty")
    for x1 in m_a:
        for x2 in x1:
            if type(x2) is not int and type(x2) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for y1 in m_b:
        for y2 in y1:
            if type(y2) is not int and type(y2) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(x3) == len(m_a[0]) for x3 in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(y3) == len(m_b[0]) for y3 in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if lenA != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_m = []
    for a in range(0, len(m_a)):
        new_l = []
        for b in range(0, lenB):
            mul = 0
            for c in range(0, lenA):
                mul += m_a[a][c] * m_b[c][b]
            new_l.append(mul)
        new_m.append(new_l)
    return new_m
