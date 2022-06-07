#!/usr/bin/python3
"""function that returns True if the object is an instance of a class
that inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """(directly or indirectly) from the specified class"""
    if type(obj) != a_class:
        return isinstance(obj, a_class)
