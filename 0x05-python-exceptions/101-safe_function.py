#!/usr/bin/python3
def safe_function(fct, *args):
    """Executes a function safely."""
    try:
        result = fct(*args)
    except Exception as e:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        result = None
    return result
