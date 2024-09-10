#!/usr/bin/env python3

# Import the function 'print_last_digit' from '9-print_last_digit' module
print_last_digit = __import__('9-print_last_digit').print_last_digit

# Call the function with 98 and 0 as arguments
print_last_digit(98)
print_last_digit(0)

# Call the function with -1024 and store the result in 'r'
r = print_last_digit(-1024)

# Print the value of 'r' (the last digit of -1024)
print(r)
