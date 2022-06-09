#!/usr/bin/python3
"""a class Student that defines a student """


class Student:
    """"defines a student"""

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance """
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            """is a list of strings, only attribute
            names contained in this list must be retrieved"""
            for x in attrs:
                """is a list of strings, only attribute names contained
                in this list must be retrieved"""
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
