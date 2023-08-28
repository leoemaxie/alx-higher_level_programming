#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers."""
    total = 0
    
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                total += 1
                print("{:d}".format(my_list[i]), end="")
        print()
        return total
    except IndexError as e:
        return total
