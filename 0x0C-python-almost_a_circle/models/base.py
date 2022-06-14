#!/usr/bin/python3
"""creating a Base class"""
import json


class Base:

    __nb_objects = 0
    """private class attribute"""

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod 
    def save_to_file(cls, list_objs):
        d = []
        file = cls.__name__+".json"
        if list_objs is None:
            with open(file, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objs))
        
        for element in list_objs:
            d.append(element.to_dictionary())
        
        with open(file, "w", encoding="utf-8")as f:
            f.write(cls.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        if not isinstance(json_string, str):
            return []
        if len(json_string) == 0:
            return []
        return json.loads(json_string)

