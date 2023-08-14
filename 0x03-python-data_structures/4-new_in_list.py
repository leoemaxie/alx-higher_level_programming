#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position"""
    if idx < 0 or idx >= len(my_list):
        return my_list

    return [e if my_list[idx] != e else element for e in my_list]
