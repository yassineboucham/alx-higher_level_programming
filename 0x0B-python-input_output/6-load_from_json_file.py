#!/usr/bin/python3
"""task 6"""
import json


def load_from_json_file(filename):
    """json"""
    with open(filename, "r", encoding="utf_8") as f:
        return json.load(f)
