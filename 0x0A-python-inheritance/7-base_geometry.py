#!/usr/bin/python3
""" creating class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
