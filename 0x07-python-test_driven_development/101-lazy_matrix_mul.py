#!/usr/bin/python3
"""function that multiplies 2 matrices by using the module NumPy"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using NumPy"""
    return numpy.matmul(m_a, m_b)
