#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    sum_a = (0 if len_a < 1 else tuple_a[0]) + (0 if len_b < 1 else tuple_b[0])
    sum_b = (0 if len_a < 2 else tuple_a[1]) + (0 if len_b < 2 else tuple_b[1])

    return (sum_a, sum_b)
