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
        inner = [str(11**i)]
        res = []
        for i in inner:
            for j in i:
                res.append(int(j))

        matrix.append(res)

    return matrix
