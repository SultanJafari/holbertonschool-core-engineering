#!/usr/bin/env python3
"""
Module for reading and printing text files using UTF-8 encoding.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to standard output.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
