#!/usr/bin/python3
"""task 1"""

def write_file(filename="", text=""):
    """write"""
    with open(filename, mode="w", encoding="utf_8") as f:
        return f.write(text)
