#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check integer validator"""

        if type(value) != int:
            """check if it is an int"""
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            """check if it is greater than 0"""
            raise ValueError("{} must be greater than 0".format(name))
