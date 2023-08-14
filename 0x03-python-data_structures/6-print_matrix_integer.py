#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    size = 0

    for array in matrix:
        size = len(array)
        for i in range(size):
            print("{:d}".format(array[i]), end=" " if i != size - 1 else "")
        print()
