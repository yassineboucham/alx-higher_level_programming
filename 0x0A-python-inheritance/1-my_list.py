#!/usr/bin/python3
"""task 1"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
