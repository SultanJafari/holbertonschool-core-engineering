#!/usr/bin/env python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size
