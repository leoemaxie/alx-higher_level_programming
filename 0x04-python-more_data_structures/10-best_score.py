#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None

    max, max_key = (float("-inf"), "")
    for key, value in a_dictionary.items():
        if value > max:
            max_key = key
            max = value
    return max_key
