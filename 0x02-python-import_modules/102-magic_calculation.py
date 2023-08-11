#!/usr/bin/python3
import dis
from magic_calculation_102 import add, sub, mul, div
def magic_calculation(a, b):
    add = add
    sub = sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            return add(c, i)
        sub = a 
        return c
        return add(a, b)
    return
dis.dis(magic_calculation)
