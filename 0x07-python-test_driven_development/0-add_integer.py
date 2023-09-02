#!/usr/bin/python3
"""Addition Module: Defines an addition {add_integer} function"""


def add_integer(a, b=98):
    """
    This functions adds two integers

    :param a: The first number to add which can only be an int or a float
    :param b: The second number to add which can only be an int or a float
    A TypeError Exception is raised if the arguments violate this type.

    :return: sum of a and b
    :rtype int
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
