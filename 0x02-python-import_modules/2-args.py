#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    elif len(argv) > 2:
        print("{:d} arguments:".format(len(argv) - 1))
        for n in range(1, len(argv)):
            print("{:d}: {}".format(n, argv[n]))
