#!/usr/bin/python3
index = 25
flag = 0

for c in range(ord('a'), ord('z') + 1):
    c += index
    index -= 2
    if flag == 1:
        flag = 0
        c -= 32
    else:
        flag = 1
    print('{}'.format(chr(c)), end='')
