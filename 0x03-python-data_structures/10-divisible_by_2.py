#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    i = 0
    list = []
    for i in my_list:
        list.append(True if i % 2 == 0 else False) 
    return list
