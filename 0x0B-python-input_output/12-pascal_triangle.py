#!/usr/bin/python3
""""
 Function that returns the pascal triangle
"""


def pascal_triangle(n):
    """
    Args:
        n: number of lines
    Returns:
        matrix: a matrix with the pascal triangle
    """

    matrix = []
    if n <= 0:
        return matrix
                    
    for i in range(n):
        inner = [','.join(str(11**i))]
        matrix.append(inner)

    return matrix
