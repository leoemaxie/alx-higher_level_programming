#!/usr/bin/python3
"""
Rectangle Module: This module constains the Rectangle Class.
"""
from base import Base


def throw_error(value, prop, flag=None):
    """Throws an Exception."""
    if not isinstance(value, int):
        raise TypeError(f"{prop} must be an integer")
    if flag is not None and value < 0:
        raise ValueError(f"{prop} must be >= 0")
    if flag is None and value <= 0:
        raise ValueError(f"{prop} must be > 0")


class Rectangle(Base):
    """
    Rectangle class with a width, height, and x,y positions. This models a
    rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        throw_error(width, "width")
        throw_error(height, "height")
        throw_error(x, "x", 1)
        throw_error(y, "y", 1)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    """Gets the {x} position property"""
    @property
    def x(self):
        return self.__x

    """Sets the {x} position  property"""
    @x.setter
    def x(self, value):
        throw_error(value, "x", 1)
        self.__x = value

    """Gets the {y} position property"""
    @property
    def y(self):
        return self.__y

    """Sets the {y} position  property"""
    @y.setter
    def y(self, value):
        throw_error(value, "y", 1)
        self.__y = value

    """Prints to stdout the square with the character #"""
    def display(self):
        for row in range(self.__height):
            if self.__x > 0:
                for pos in range(self.__y):
                    print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    """Calculates the area of the Rectangle"""
    def area(self):
        return self.__width * self.__height

    """Returns a string of a rectangle."""
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    """Updates the Rectangle class"""
    def update(self, *args, **kwargs):
        if len(args) > 5:
            raise Exception("Too many arguments")
        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        else:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    """Returns the dictionary representation of a rectangle"""
    def to_dictionary(self):
        return self.__dict__
