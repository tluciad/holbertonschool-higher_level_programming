#!/usr/bin/python3
"""a function that returns the dictionary description
with simple data structure"""


def pascal_triangle(n):
    """Returns an empty list if n <= 0"""
    if n <= 0:
        return []

    arr = []
    for i in range(n):
        if i == 0:
            arr.append([1])
            continue
        row = []
        for j in range(i + 1):
            row.append(j)
        for j in range(1, i):
            row[0] = 1
            row[i] = 1
            row[j] = arr[i-1][j] + arr[i - 1][j - 1]
        arr.append(row)

    return arr
