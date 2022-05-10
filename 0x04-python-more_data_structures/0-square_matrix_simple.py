#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    N_matrix = [[j**2 for j in matrix[i]] for i in range(len(matrix))]
    return N_matrix
