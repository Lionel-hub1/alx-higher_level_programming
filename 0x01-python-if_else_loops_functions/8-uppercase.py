#!/usr/bin/python
def uppercase(str):
    for char in str:
        if 97 <= ord(char) < 123:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
