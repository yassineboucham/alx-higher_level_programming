#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    i = 0
    list = []
    while i < my_list:
        list.append(True if my_list[i] % 2 == 0 else False)
        i += 1
    return list
