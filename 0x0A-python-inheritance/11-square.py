#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """"Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        """area() method must be implemented"""
        super().__init__(size, size)

    def __str__(self):
        """should print, and str() should return,
        the square description: [Square] <width>/<height>"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
