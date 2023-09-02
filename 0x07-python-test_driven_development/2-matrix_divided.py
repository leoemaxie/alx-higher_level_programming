#!/usr/bin/python3
"""Matrix Divided Module: Defines an addition {matrix_divided} function"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.

    :param matrix: A list of lists of integers or floats
    :param div: A number (integer or float),
    A TypeError Exception is raised if any of the arguments violate this type.

    :return: a new matrix
    :rtype list
    """
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("a must be an integer")

    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")

    return a + b
