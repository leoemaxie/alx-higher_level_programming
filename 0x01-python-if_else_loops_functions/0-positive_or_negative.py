#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
msg = ''

if number > 0:
    msg = 'positive'
elif number == 0:
    msg = "zero"
else:
    msg = 'negative'

print(f'{number} is {msg}')
