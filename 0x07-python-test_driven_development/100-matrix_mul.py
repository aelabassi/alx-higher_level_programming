#!/usr/bin/python3
"""
This module that have a function that mulltiply two matrices

"""


def matrix_mul(m_a, m_b):
    """ This function multiplies two matrices
        Args:
            m_a (list of lists): matrix of ints or floats
            m_b (list of lists): matrix of ints or floats
        Raises:
            TypeError: if m_a and m_b is not list of lists
            ValueError: m_a and m_a should contain integers
            or floats
            TypeError: rows with the same size
            ValueError: m_a and m_a don't have same
            row size
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can0t be empty")
    if not all((isinstance(el, int) or isinstance(el, float))
       for el in [i for row in m_a for i in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(el, int) or isinstance(el, float))
       for el in [i for row in m_b for i in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    new_m = [[0]*len(m_b[0]) for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_m[i][j] += m_a[i][k]*m_b[k][j]
    return new_m
