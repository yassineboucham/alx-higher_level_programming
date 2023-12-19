#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = 0
    try:
        res = fct(*args)
    except (ZeroDivisionError, IndexError) as e:
        print("Exception: ", e, file=sys.stderr)
        res = None
    return (res)
