#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()."""
    try:
        value / 10
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
