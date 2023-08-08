#!/usr/bin/python3
import random

number = random.randint(-10, 10)
msg = ''

if number > 0:
    msg = 'positive'
elif number == 0:
    msg = "zero"
else:
    msg = 'negative'

print(f'{number} is {msg}')
