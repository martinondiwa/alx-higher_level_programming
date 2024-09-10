#!/usr/bin/python3
import random

# Generate a random integer between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive, zero, or negative
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
