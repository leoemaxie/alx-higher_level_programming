#!/usr/bin/python3
"""
Base Module: This module will be the base of all other classes in this project.
"""
import csv
import json


class Base:
    __nb_objects = 0

    """
    ---------------------------- BASE TEST CLASS ------------------------------
    The goal of it is to manage id attribute in all future classes and to avoid
    duplicating the same code (by extension, same bugs)
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """Returns the JSON string representation of list_dictionaries"""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    """Returns the list of the JSON string representation json_string"""
    @classmethod
    def from_json_string(json_string):
        if json_string:
            return json.load(json_string)
        return []

    """Writes the JSON string representation of list_objs to a file"""
    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", 'w') as file:
            file.write(cls.to_json_string(list_objs))

    """Readsthe JSON string representation of list_objs to a file"""
    @classmethod
    def load_from_file(cls):
        try:
            with open(f"{cls.__name__}.json", 'r') as file:
                return cls.to_json_string(file.read())
        except FileNotFoundError:
            return []

    """Serializes data from CSV"""
    @classmethod
    def save_to_file_csv(cls):
        with open(f"{cls.__name__}.csv", 'w') as file:
            writer = csv.writer(file)
            writer.write(cls.__dict__.values())

    """Deserializes data from CSV"""
    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(f"{cls.__name__}.csv", 'r') as file:
                return csv.reader(file)
        except FileNotFoundError:
            return []
