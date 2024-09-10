#!/usr/bin/python3

# Loop through ASCII values of lowercase letters (a to z)
for i in range(97, 123):
    # Skip the letters 'e' (ASCII 101) and 'q' (ASCII 113)
    if (i == 101) or (i == 113):
        continue
    # Print the character corresponding to the ASCII value
    print(chr(i), end="")
