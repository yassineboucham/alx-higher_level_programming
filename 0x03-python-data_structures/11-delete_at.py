#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 > idx or idx > len(my_list) or my_list is None:
        return my_list
    elif len(my_list) is idx:
        my_list[:] = my_list[:idx - 1]
    else:
        del my_list[idx]
    return my_list
