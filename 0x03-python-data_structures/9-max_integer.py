#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_val = my_list[0]
    for list in my_list:
        if (max_val < list):
            max_val = list
    return max_val
