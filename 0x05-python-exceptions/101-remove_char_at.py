#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if n < 0 or len(str) <= n:
        return str
    for c in str:
        if c != str[n]:
            new_str += c
    return new_str
