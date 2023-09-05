#!/usr/bin/python3
"""
Rectangle Module: Defines a Rectangle class with a private variable {width}
{height}and various methods that works on them. Handles Exceptions.
"""


def throw_error(value, prop):
    """Throws an Exception."""
    if not isinstance(value, int):
        raise TypeError(f"{prop} must be an integer")
    if value < 0:
        raise ValueError(f"{prop} must be >= 0")


class Rectangle:
    """
    A Rectangle class with defined width and height. Raises an Exceptions
    if {width} or {height} doesn't meet the criteria.
    """
    def __init__(self, width=0, height=0):
        throw_error(width, "width")
        throw_error(height, "height")
        self.__width = width
        self.__height = height

    """Gets the {width} property"""
    @property
    def width(self):
        return self.__width

    """Sets the {width} property"""
    @width.setter
    def width(self, value):
        throw_error(value, "width")
        self.__width = value

    """Gets the {height} property"""
    @property
    def height(self):
        return self.__height

    """Sets the {height} property"""
    @height.setter
    def height(self, value):
        throw_error(value, "height")
        self.__height = value

    """Calculates the area of the Rectangle"""
    def area(self):
        return self.__width * self.__height

    """Calculates the perimeter of the Rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
