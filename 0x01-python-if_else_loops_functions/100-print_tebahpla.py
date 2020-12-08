#!/usr/bin/python3
for num in reversed(range(97, 123)):
    if num % 2 != 0:
        num -= 32
    print("{}".format(chr(num)), end="")
