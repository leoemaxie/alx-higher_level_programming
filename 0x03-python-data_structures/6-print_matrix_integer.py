#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for array in matrix:
        for elem in array:
            print("{:d}".format(elem), end=" " if elem != elem[-1] else "")
        print()
