#!/usr/bin/env python3
safe_print_integer = __import__('safe_print_integer').safe_print_integer

value = 89
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))

value = -89
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))
