#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    j = 0
    s = ""
    for i in a_dictionary:
        if a_dictionary[i] > j:
            j = a_dictionary[i]
            s = i
    return s
