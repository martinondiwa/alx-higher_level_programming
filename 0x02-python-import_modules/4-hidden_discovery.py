#!/usr/bin/python3
# This script prints all names defined by the hidden_4 module, excluding those starting with '__'.

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    # Get a list of all names defined by hidden_4
    names = dir(hidden_4)

    # Loop through the names and print those that don't start with '__'
    for name in names:
        if name[:2] != "__":
            print(name)
