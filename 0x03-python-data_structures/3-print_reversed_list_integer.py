#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order"""
    size = 0
    if my_list:
        size = len(my_list)
        if size > 0:
            for i in range(size - 1, -1, -1):
                print("{:d}".format(my_list[i]))
