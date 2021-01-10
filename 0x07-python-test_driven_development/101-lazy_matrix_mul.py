#!/usr/bin/python3
"""
7. Lazy matrix multiplication
Write a function that multiplies 2 matrices by using the module NumPy.
Prototype: def lazy_matrix_mul(m_a, m_b):
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy.
    """
    return numpy.matmul(m_a, m_b)
