#!/usr/bin/python3
import dis
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div

def magic_calculation(a, b):
    add(a, b)
dis.dis(magic_calculation)
