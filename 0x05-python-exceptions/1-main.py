#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
arr = [9]
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
has_been_print = safe_print_integer(arr)
if not has_been_print:
    print("{} is not an integer".format(arr))