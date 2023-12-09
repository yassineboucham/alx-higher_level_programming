#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    return (list(map(lambda index: index if index != search else replace, my_list)))