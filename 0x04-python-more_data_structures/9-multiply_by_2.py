#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list = {}
    for key, value in a_dictionary.items():
        list[key] = value * 2
    return list
