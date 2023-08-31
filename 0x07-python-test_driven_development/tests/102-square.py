#!/usr/bin/python3
"""Square Moduule: Defines a Square class with a private variable {size} and
various methods that works on {size}. Handles Exceptions.
"""


class Square:
    """A square class with defined size. Raises an Exceptions if {size} doesn't
    meet the criteria
    Square instance can answer to comparators: ==, !=, >, >=, < and <= based
    on the square area
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.area = size ** 2

    """Checks whether the area of two Square objects are equal"""
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area == other.area

    """Checks whether the area of two Square objects are not equal"""
    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area != other.area
    """Checks whether the area of a Square object is greater than the 
       area of another Square object
    """
    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area > other.area

    """Checks whether the area of a Square object is greater than
       or equals the area of another Square object
    """
    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area >= other.area

    """Checks whether the area of a Square object is less than
       or equals the area of another Square object
    """
    def __le__(self, other):
        if isinstance(other, Square):
            return self.area <= other.area

    """Checks whether the area of a Square object is less than
       the area of another Square object
    """
    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area < other.area
    """Checks whether the area of a Square object is less than
       or equals the area of another Square object
    """
    def __le__(self, other):
        if isinstance(other, Square):
            return self.area <= other.area

    @property
    def size(self):
        return self.__size

    """Sets the {size} property"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Calculates the area of the square"""
    def area(self):
        return self.area

s_5 = Square(6)
s_6 = Square(3)

if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
