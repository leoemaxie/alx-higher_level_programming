#!/usr/bin/python3
if __name__ == "__main__":
    """ Prints the result of the addition of all commandline arguments """
    import sys

    args_len = len(sys.argv)
    sum = 0

    for i in range(1, args_len):
        sum += int(sys.argv[i])

    if args_len > 1:
        print("{}".format(sum))

    sys.exit(0)
