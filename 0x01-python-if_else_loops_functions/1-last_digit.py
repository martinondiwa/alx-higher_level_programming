#!/usr/bin/python3
import random

# Generate a random integer between -10000 and 10000
number = random.randint(-10000, 10000)

# Determine the last digit of the number
if number < 0:
    last_num = number % -10
else:
    last_num = number % 10

# Print the appropriate message based on the value of the last digit
if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
