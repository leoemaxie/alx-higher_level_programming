#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer"""
    try:
        print("{:d}".format(value))
    except ValueError as e:
        import sys
        sys.stderr.write("Exception: {}\n".format(e))
        return False
    else:
        return True
