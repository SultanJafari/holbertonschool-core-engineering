#!/usr/bin/env python3
import random

number = __import__('random').randint(-10, 10) # يعطينا ارقام عشوائية من هذه التحديد او الارقام اللي انت تحتاجها
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
