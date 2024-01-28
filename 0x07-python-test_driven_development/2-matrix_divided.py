#!/usr/bin/python3
"""
This function devides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """This function divides all elements of the matrix `matrix`
        Args:
            matrix (list of lists): The matrix
            div (int or float): positive real number (>0)
        Return:
            matrix: all elements are divided by div
    """
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)
            or matrix == [] or not all((isinstance(el, int)
            or isinstance(el, float))
            for el in [i for row in matrix for i in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda col: round(col/div, 2), row)) for row in matrix]