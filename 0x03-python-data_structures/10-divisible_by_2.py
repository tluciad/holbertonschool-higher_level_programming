#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            i.append(True)
        else:
            i.append(False)
    return i
