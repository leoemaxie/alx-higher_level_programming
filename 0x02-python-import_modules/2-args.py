#!/usr/bin/python3
import sys

# Excludes the name of tge program
args_len = len(sys.argv) - 1
msg = "argument" if args_len == 1 else "arguments"
print("{} {}".format(args_len, msg), end=":\n" if args_len > 0 else ".\n")

for i in range(1, args_len + 1):
    print("{}: {}".format(i, sys.argv[i]))

sys.exit(0)