#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    total = 0
    for i in range(x):
        try:
            total += 1
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
    print()
    return total
