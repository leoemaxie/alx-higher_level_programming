#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    total = 0
    
    try:
        for i in range(x):
            total += 1
            print("{}".format(my_list[i]), end="")
        print()
        return total
    except IndexError:
        return total
