#!/usr/bin/python3
"""Square Moduule: Defines a Square class with a private variable {size} and
various methods that works on {size}. Also includes the private variable
{position}. Handles Exceptions.
"""


class Square:
    """A square class with defined size. Raises an Exceptions if {size} or
    {position} doesn't meet the criteria
    """
    def __init__(self, size=0, position=(0, 0)):
        if not type(size).isinstance(int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not type(position).isinstance(tuple):
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    """Gets the {size} property"""
    @property
    def size(self):
        return self.__size

    """Sets the {size} property"""
    @size.setter
    def size(self, value):
        if not type(value).isinstance(int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Gets the {position} property"""
    @property
    def position(self):
        return self.__position

    """Sets the {position} property"""
    @position.setter
    def size(self, value):
        if not type(value).isinstance(tuple):
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """Calculates the area of the square"""
    def area(self):
        return self.__size ** 2

    """Prints to stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                if self.__position[1] >= 0:
                    for pos in range(self.__position[0]):
                        print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
