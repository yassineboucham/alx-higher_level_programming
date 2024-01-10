#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf_8") as f:
        return f.read()
    # The following line will never be reached, so it can be removed
    # f.closed
