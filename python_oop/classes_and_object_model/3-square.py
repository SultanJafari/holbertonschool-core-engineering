#!/usr/bin/env python3
"""Defines a square."""


class Square:
    """SUltan."""

    def __init__ (self, size=0):
        self.__size = size
    def area (self):
        """Defines a square."""
        return self.__size * self.__size
