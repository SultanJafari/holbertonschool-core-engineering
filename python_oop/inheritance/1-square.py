#!/usr/bin/env python3
"""Defines the Square class."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize the square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
