#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b = 0
        for k, v in a_dictionary.items():
            if v >= b:
                b = v
                key = k
        return key
