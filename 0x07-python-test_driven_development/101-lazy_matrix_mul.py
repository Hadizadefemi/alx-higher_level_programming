#!/usr/bin/python3
""" Module 101-lazy_matrix_mul
function that multiplies 2 matrices by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        m_a * m_b
    """

    m1 = numpy.matrix(m_a)
    m2 = numpy.matrix(m_b)

    return m1 * m2
