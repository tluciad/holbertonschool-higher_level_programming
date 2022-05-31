#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix[0]) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix[0][0]) != int and type(matrix[0][0]) != float:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
