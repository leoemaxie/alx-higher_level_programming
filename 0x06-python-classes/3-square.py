#!/usr/bin/python3
"""Square Moduule: Defines a Square class with a private variable {size} and
method {area}. Handles Exceptions
"""


class Square:
    """A square class with defined size. Raises an Exceptions if {size} doesn't
    meet the criteria
    """
    def __init__(self, size=0):
        if not type(size).isinstance(int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Calculates the area of the square"""
    def area(self):
        return self.__size ** 2
