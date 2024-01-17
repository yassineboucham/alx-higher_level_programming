#!/usr/bin/python3
"""

base


"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """to_json_string"""
        dp = json.dumps(list_dictionaries)
        if dp is not (None, []):
            return dp
