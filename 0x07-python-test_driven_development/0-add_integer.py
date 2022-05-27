#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b"""
    if type(a) != int and type(a) != float:
        """to verify that a is a number"""
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        """to verify that is a number"""
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a+b
