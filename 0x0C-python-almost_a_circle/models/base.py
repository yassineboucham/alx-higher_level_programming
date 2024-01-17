#!/usr/bin/python3
"""

base


"""
import json
import csv
import os.path


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
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        save_list = []
        if not list_objs:
            pass
        else:
            for obj in list_objs:
                save_list.append(obj.to_dictionary())
            with open("{}.json".format(cls.__name__), "w", encoding="utf_8") as f:
                f.write(cls.to_json_string(save_list))
