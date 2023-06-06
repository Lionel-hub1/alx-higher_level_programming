#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if last_digit >= 6:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {ld} and is 0")
elif 0 < last_digit < 6:
    if number < 0:
        print(f"Last digit of {number} is {-ld} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
