#!/usr/bin/python3
"""Square Moduule: Defines a Square class with a private variable {size} and
handles Exceptions
"""


class Square:
    """A square class with defined size. Raises an Exceptions if {size} doesn't
    meet the criteria
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
