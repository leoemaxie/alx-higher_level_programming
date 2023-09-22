#!/usr/bin/python3
"""
Square Module: This module constains the Square Class.
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Square class with a size and x,y positions. This models a square and
    inherits from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """Gets the {size} property"""
    @property
    def size(self):
        return self.width

    """Sets the {size} property"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height  = value

    """Returns a string of a square."""
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )
