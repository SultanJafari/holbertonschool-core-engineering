#!/usr/bin/env python3
"""Defines mixins and a Dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the swimming ability."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the flying ability."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon with swimming and flying abilities."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
