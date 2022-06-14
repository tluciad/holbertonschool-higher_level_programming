#!/usr/bin/python3
"""creating a Base class"""
import json


class Base:
    """base class of the models"""

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
        """adding the static method that
         returns the list of the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ adding the class method that writes the JSON
        string representation"""
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

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            d = cls(4, 2, 1)

        if cls.__name__ == "Square":
            d = cls(2, 2)
        d.update(**dictionary)
        return d

    @classmethod
    def load_from_file(cls):
        list = []
        with open(cls.__name__ + ".json", "r", encoding='utf-8') as f:
            list = cls.from_json_string(f.read())
        list2 = []
        for i in list:
            if type(i) is dict:
                list2.append(cls.create(**i))
            else:
                list2.append(i)
        return list2
