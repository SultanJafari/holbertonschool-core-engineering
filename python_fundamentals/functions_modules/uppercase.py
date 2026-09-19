#!/usr/bin/env python3
def uppercase(text):
    new_str = ""
    for i in text:
        if ord("a") <= ord(i) <= ord("z"):
            new_str += chr(ord(i) - 32)
        else:
            new_str += i
    print(new_str)
