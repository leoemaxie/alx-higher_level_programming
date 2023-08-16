#!/usr/bin/python3
def complex_delete(a_dictionary, del_value):
    """Deletes keys with a specific value in a dictionary."""
    for key, value in a_dictionary.items():
        if value == del_value:
            del a_dictionary[key]
    return a_dictionary
