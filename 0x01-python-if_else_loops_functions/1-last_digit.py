#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastA = (number * -1) % 10
elif number >= 0:
    lastA = number % 10

if lastA > 5:
    print("Last digit of {:d} ".format(number), end="")
    print("is {:d} and is greater than 5".format(lastA))
elif lastA == 0:
    print("Last digit of {:d} ".format(number), end="")
    print("is {:d} and is 0".format(lastA))
elif lastA < 6:
    print("Last digit of {:d} ".format(lastA), end="")
    print("is {:d} and is less than 6 and not 0".format(lastA))
