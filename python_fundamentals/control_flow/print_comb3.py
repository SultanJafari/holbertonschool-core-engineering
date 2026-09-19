#!/usr/bin/env python3
for i in range(9):
    for j in range(i + 1, 10):
        print("{:02d}".format(i, j), end=", " if i < 8 else "\n")
