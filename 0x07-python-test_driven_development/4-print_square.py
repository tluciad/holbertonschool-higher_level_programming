#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    if type(size) != int:
        """size must be an integer"""
        raise TypeError("size must be an integer")
    if size < 0:
        """size must be most than 0"""
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
