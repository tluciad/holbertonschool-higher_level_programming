#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 4-rectangle.py)"""


class Rectangle:
    """empty class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property def width(self): to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property def height(self): to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return(self.__height*self.__width)

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return((self.__width*2)+(self.__height*2))

    def __str__(self):
        """should print the rectangle with the character #"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height):
            str += ("#"*self.__width) + "\n"
        return str[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """an instance of Rectangle is deleted"""
        print("Bye rectangle...")
