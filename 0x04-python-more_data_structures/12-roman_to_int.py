#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
           'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
           'DM': 900, 'M': 1000}
    res = 0
    i = 0
    if rom is not None and type(roman_string) is str:
        while i < len(roman_string):
            if rom.get(roman_string[i: i+2]) is not None:
                res += rom[roman_string[i: i+2]]
                i += 2
            else:
                res += rom[roman_string[i]]
                i += 1
    return res
