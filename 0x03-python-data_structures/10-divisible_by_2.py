#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == None:
        return None
    i = 0
    list = []
    while i < len(my_list):
        list.append(True if my_list[i] % 2 == 0 else False) 
        i += 1
    return list
