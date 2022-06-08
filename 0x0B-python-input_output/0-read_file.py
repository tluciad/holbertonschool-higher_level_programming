#!/usr/bin/python3
"""function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """Prototype of function"""
    with open(filename, 'r', encoding="utf-8") as f:
        """must use the with statement"""
        print(f.read(), end="")
