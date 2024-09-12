#!/usr/bin/python3
# This script prints "#pythoniscool" using os.write and encoding it to UTF-8.

__import__("os").write(1, "#pythoniscool\n".encode("UTF-8"))
