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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is not None or list_dictionaries != "[]":
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        if list_objs is not None:
                list = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "a", encoding="utf_8") as f:
            f.write(cls.to_json_string(list))
