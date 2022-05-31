#!/usr/bin/python3
""" a class that defines a square by: (based on 5-square.py)"""


class Square:
    """Creating the class square"""

    def __init__(self, size=0, position=(0, 0)):
        """private instance atribute: size and position"""
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """position as a property"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the value of position"""
        if type(value) != tuple:
            """must be a tuple of 2 positive integers"""
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            """must be 2 integers"""
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            "must be positive integers"
            if type(i) != int:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print()
        for i in range(0, self.__size):
            for j in range(self.size):
                print("#", end="")
            for x in range(self.position[0]):
                print(" ", end="")
            print("")
