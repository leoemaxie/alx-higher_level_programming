#!/usr/bin/python3
"""Say My Name Module: Defines {say_my_name} function"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    :param first_name: The first name of the user.
    :param last_name: The last name of the user.
    Both arguments must be a string, otherwise a TypeError exception is raised
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
