#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    i = 0
    for dic in a_dictionary:
        if dic[0] is key:
            dic[1] = value
            i += 1
    if i is 0:
        a_dictionary[key] = value
    return a_dictionary
