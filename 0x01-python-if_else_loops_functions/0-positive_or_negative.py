#!/usr/bin/python3
import random

num = random.randint(-10000, 10000)
msg = ''

if num > 0:
    msg = 'positive'
elif num == 0:
    msg = "zero"
else:
    msg = 'negative'

print(f'{num} is {msg}')
