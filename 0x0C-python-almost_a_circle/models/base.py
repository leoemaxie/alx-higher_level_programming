#!/usr/bin/python3
"""
Base Module: This module will be the base of all other classes in this project.
"""


class Base:
    __nb_objects = 0

    """
    -------------------- BASE TEST CLASS ------------------
    The goal of it is to manage id attribute in all future classes and to avoid
    duplicating the same code (by extension, same bugs)
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
