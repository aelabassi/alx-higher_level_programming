#!/usr/bin/python3
"""
This module uses numpy to calculate the product of two matrices

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ returns the matrix product (vactorization) """
    return np.matmul(m_a, m_b)
