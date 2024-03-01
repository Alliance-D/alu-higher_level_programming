#!/usr/bin/python3
# prints string in uppercase
uppercase_str = ""
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += c
    print("{}".format(uppercase_str))
