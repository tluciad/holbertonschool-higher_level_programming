#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    result = 0
    for i in my_list:
        if i not in new:
            new.append(i)
    for j in new:
        result += j
    return result
