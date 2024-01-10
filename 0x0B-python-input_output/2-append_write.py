#!/usr/bin/python3
"""tasks 2"""


def append_write(filename="", text=""):
    """append"""
    with open(filename, "a", encoding="utf_8") as f:
        return f.write(text)
