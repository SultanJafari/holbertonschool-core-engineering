#!/usr/bin/env python3

result = ""
for i in range (ord("a"), ord("z")+ 1):
    c = chr(i)
    if c != 'e' and c != 'q':
        result += c
print (result, end='')
