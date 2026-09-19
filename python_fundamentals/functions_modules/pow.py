#!/usr/bin/env python3


def pow(a, b):
    """Return the value of a raised to the power of b."""
    if b == 0:
        return 1

    result = 1
    exponent = b if b > 0 else -b

    for _ in range(exponent):
        result *= a

    if b < 0:
        return 1 / result
    return result
