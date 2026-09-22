#!/usr/bin/env python3
"""Defines a square."""


class Square:
    """Represents a square."""

    @property
    def __init__(self, size=0):
        self.self = size

    def size(self, size=0):
        return self.__size
    @size.setter
    def size(self, value):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
