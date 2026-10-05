#!/usr/bin/env python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size  # استدعاء الـ setter للتحقق من القيمة الأولية

    @property
    def size(self):
        """Getter to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to validate and set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size
