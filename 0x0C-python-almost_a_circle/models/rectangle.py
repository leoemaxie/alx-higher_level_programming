#!/usr/bin/python3
"""
Rectangle Module: This module constains the Rectangle Class.
"""
from base import Base


def throw_error(value, prop):
    """Throws an Exception."""
    if not isinstance(value, int):
        raise TypeError(f"{prop} must be an integer")
    if value < 0:
        raise ValueError(f"{prop} must be >= 0")


class Rectangle(Base):
    """
    Rectangle class with a width, height, and x,y positions. This models a
    rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        throw_error(width, "width")
        throw_error(height, "height")
        throw_error(x, "x")
        throw_error(x, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """{width} getter"""
    @property
    def width(self):
        return self.__width

    """Sets the {width} property"""
    @width.setter
    def width(self, value):
        throw_error(value, "width")
        self.__width = value

    """Sets the {height} property"""
    @property
    def height(self):
        return self.__height

    """Sets the {height} property"""
    @height.setter
    def height(self, value):
        throw_error(value, "height")
        self.__height = value

    """Gets the {x} position property"""
    @property
    def x(self):
        return self.__x

    """Sets the {x} position  property"""
    @x.setter
    def x(self, value):
        throw_error(value, "x")
        self.__x = value

    """Gets the {y} position property"""
    @property
    def y(self):
        return self.__y

    """Sets the {y} position  property"""
    @y.setter
    def y(self, value):
        throw_error(value, "y")
        self.__y = value

    def display(self):
        for row in range(self.__height):
            for col in range(self.__width):
                print("#", end="")
            print("\n")

    """Calculates the area of the Rectangle"""
    def area(self):
        return self.__width * self.__height

    """Returns a string of a rectangle."""
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x
            self.__y
            self.__width
            self.__y
        )
