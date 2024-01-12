#!/usr/bin/python3
"""task 5"""
import json


def save_to_json_file(my_obj, filename):
    """json"""
    with open(filename, "w", encoding="utf_8") as f:
        f.write(json.dumps(my_obj))
