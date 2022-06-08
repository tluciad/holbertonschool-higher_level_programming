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
