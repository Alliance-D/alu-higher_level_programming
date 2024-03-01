#!/usr/bin/python3
# prints possible combinations of 2 digit numbers
for i in range(10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9 and i != j:
            print("{}{}".format(i, j), end=", ")
        else:
            print("{}{}".format(i, j), end="")
