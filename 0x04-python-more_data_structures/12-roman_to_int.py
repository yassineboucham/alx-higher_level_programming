#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    number = 0
    i = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1 and roman_string[i: i + 2] == 'IV':
            number += 4
            i += 2
        elif i < len(roman_string) - 1 and roman_string[i: i + 2] == 'IX':
            number += 9
            i += 2
        else:
            if roman_string[i] == 'I':
                number += 1
            elif roman_string[i] == 'V':
                number += 5
            elif roman_string[i] == 'X':
                number += 10
            elif roman_string[i] == 'L':
                number += 50
            elif roman_string[i] == 'C':
                number += 100
            elif roman_string[i] == 'D':
                number += 500
            elif roman_string[i] == 'M':
                number += 1000
            i += 1
    return number
