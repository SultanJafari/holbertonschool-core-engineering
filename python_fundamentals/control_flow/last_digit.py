
number = __import__('random').randint(-10000, 10000)

last_digit = number % 10 
print(last_digit, number )

if last_digit > 5:
    print("last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("last digit of", number, "is", last_digit, "and is 0")
elif last_digit < 6 and last_digit != 0:
    print("last digit of", number, "is", last_digit, "and is is greater than 6 and not 0")