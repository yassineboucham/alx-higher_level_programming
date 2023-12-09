#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    see = []
    for i in my_list:
        if i not in see:
            res += i
            see.append(i)
    return res

