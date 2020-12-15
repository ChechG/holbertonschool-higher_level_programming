#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(0, length):
        len2 = len(matrix[i])
        for j in range(0, len2):
            print("{:d}".format(matrix[i][j]), end="")
            if j < len2 - 1:
                print(" ", end="")
        print("")
