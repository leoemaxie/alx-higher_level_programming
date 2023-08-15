#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Creates a new list from my_list with the element of my_list replaced at a specific position"""
    if idx < 0 or idx >= len(my_list):
        return my_list

    return [e if my_list[idx] != e else element for e in my_list]
