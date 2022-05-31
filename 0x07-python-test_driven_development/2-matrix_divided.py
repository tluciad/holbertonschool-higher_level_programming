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
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix
