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


def str_rectangle(width, height):
    """
    Returns a string of # character based on a Rectangle's width and height.
    """
    if width == 0 or height == 0:
        return ""
    rectangle = ""
    for row in range(height):
        for col in range(width):
            rectangle += '#'
        if row < height - 1:
            rectangle += '\n'
    return rectangle


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

    """
    Returns a string of # character based on a Rectangle's width and height.
    """
    def __str__(self):
        return str_rectangle(self.__width, self.__height)

    """Returns a string representation of a Rectangle instance."""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """Prints a short message when an instance of Rectangle is deleted."""
    def __del__:
        print("Bye rectangle...")
