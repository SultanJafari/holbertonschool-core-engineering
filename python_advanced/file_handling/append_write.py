#!/usr/bin/env python3
"""
Module for writting and printing text files using UTF-8 encoding.
"""


def append_write(filename="", text=""):
    """
    write a text file and prints its content to standard output.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.append(a))
