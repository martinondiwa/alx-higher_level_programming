#!/usr/bin/python3
# Initialize the string with a description of Python
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"

# Extract and concatenate substrings
# First extract: "object-oriented programming" (index 39 to 67)
# Second extract: "with " (index 107 to 112)
# Third extract: "Python" (first 6 characters)
str = str[39:67] + str[107:112] + str[:6]

# Print the resulting concatenated string
print(str)
