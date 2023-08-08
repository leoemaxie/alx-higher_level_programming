#!/usr/bin/python3
for num in range(0, 10):
    for unit in range(num, 10):
        if unit != num:
            print("{}{}".format(num, unit),
                  end=", " if unit + num != 17 else "\n")
