#!/usr/bin/python3

# Loop through numbers from 0 to 98
for i in range(99):
    # Print each number with leading zeros and followed by a comma and space
    print("{:02d}".format(i), end=", ")

# Print the number 99 without a trailing comma
print("{:02d}".format(99))
