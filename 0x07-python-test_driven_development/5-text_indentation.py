#!/usr/bin/python3
"""function that prints a text with 2 new lines after
each of these characters: ., ? and :"""


def text_indentation(text):
    if type(text) != str:
        """text must be a string"""
        raise TypeError("text must be a string")
    else:
        newtxt = text
        newtxt = newtxt.replace(".", ".\n\n")
        newtxt = newtxt.replace(",", ",\n\n")
        newtxt = newtxt.replace(":", ":\n\n")
        newtxt = newtxt.split("\n")
    for line in newtxt:
        line = line.strip()
        print(line + "\n", end="")
