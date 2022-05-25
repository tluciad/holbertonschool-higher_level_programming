#!/usr/bin/python3
"""a class that defines a square by: (based on 4-square.py)"""


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

    def area(self):
        """Public instance method"""
        a = self.__size*self.__size
        """to return the area"""
        return a

    @property
    def size(self):
        """size as a property"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size"""
        if type(value) != int:
            """size must be an integer"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """size must be most than 0"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method"""
        a = self.__size*self.__size
        """to return the area"""
        return a

    def my_print(self):
        """Public instance method to  prints in stdout
        the square with the character #"""
        if self.__size == 0:
            """if size is equal to 0 print an empty line"""
            print("")
        for i in range(self.__size):
            for j in range(self.size):
                print("#", end="")
            print("")
