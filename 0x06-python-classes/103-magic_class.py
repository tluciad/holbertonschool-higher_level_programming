#!/usr/bin/python3
"""import module"""
import math


class MagicClass:
    """creating a class"""

    def __init__(self, radius=0):
        """private instance radius"""
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            """must be a number"""
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """to calculate the area of circumference"""
        return (self.__radius**2)*math.pi

    def circumference(self):
        """to calculate the circumference"""
        return 2*math.pi*self.__radius
