#!/usr/bin/python3
"""a class that defines a square by: (based on 1-square.py)"""


class Square:
    """Creating the class square"""

    def __init__(self, size=0):
        """defining a private instance atribute: size"""
        if type(size) != int:
            """size must be an integer"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """size must be most than 0"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
