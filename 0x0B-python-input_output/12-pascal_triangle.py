#!/usr/bin/python3
""" Pascal triangle """


def pascal_triangle(n):
    """ Pascal triangle """
    new_list = []
    if n <= 0:
        return new_list
    for line in range(0, n):
        row = []
        for i in range(0, line + 1):
            res = 1
            k = i
            j = line
            if (k > j - k):
                k = j - k
            for l in range(0, k):
                res = res * (j - l)
                res = res // (l + 1)
            row.append(res)
        new_list.append(list(row))
    return new_list
