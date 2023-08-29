#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely."""
    try:
        return fct(*args)
    except BaseException as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
