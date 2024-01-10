#!/usr/bin/python3
"""task 0"""


def read_file(filename=""):
    """print file"""
    with open(filename, encoding="utf_8") as f:
        return print(f.read())
