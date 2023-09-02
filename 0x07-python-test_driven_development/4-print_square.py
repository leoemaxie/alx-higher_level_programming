#!/usr/bin/python3
"""Print Square Module: Defines {print_square} function"""


def print_square(size):
    """
    Prints a square with the character #.

    :param size: The size length of the square. {size} must be an integer,
    otherwise a TypeError exception is raised
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()

