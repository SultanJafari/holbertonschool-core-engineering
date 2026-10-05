#!/usr/bin/env python3
"""
Module to read and print a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
