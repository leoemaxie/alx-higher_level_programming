#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    return [elem if elem != search else replace for elem in my_list]
