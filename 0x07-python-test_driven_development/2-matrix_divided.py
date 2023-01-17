#!/usr/bin.python3
""" Module 2-matrix_divided
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix
    Args:
        matrix: list of list
        div: number used to divide matrix
    Returns:
        a new matrix
    Raises:
        TypeError: if matrix is not a list of list
                   if row of matrix not the same size
                   if div is not an integer

        ZeroDivisionError: if div is zero
    """

    m = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(m)

    if type(matrix) is list:
        for rows in matrix:
            if type(rows) != list:
                raise TypeError(m)
            for j in rows:
                if type(j) not in [int, float]:
                    raise TypeError(m)

        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i+1]):
                m = "Each row of the matrix must have the same size"
                raise TypeError(m)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        rows = []
        for j in row:
            rows.append(round(j / div, 2))
        new_matrix.append(rows)

    return new_matrix
