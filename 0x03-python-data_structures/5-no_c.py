#!/usr/bin/env python3
def no_c(my_string):
    str = ""
    for i in my_string:
        if i != "C" and i != "c":
            str += i
    return str
