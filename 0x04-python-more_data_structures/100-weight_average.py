#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>)."""
    weight, divisor, multiplier  = (0, 0, 1)

    if not my_list:
        return 0
    for tup in my_list:
        for elem in tup:
            multiplier *= elem
        weight += multiplier
        multiplier = 1
        divisor += tup[-1]
    return weight / divisor
