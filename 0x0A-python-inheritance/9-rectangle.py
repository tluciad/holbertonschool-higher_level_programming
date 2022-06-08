#!/usr/bin/python3
"""class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method must be implemented"""
        return(self.__height*self.__width)

    def __str__(self):
        """return, the following rectangle
        description: [Rectangle] <width>/<height>"""
        return("[Rectangle] {}/{}".format(self.__height, self.__width))
