#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = a_dictionary
    for ad in sorted(dic.items()):
        print("{}: {}".format(ad[0], ad[1]))