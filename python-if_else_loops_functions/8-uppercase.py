#!/usr/bin/python3
#prints string in uppercase
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32), end="")
                    print()
