#!/usr/bin/python3
"""
3. Print square
Write a function that prints a square with the character #.
Prototype: def print_square(size):
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
