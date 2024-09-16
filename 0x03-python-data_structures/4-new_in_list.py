#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Creates a new list with an element replaced at a specified index.

    Args:
        my_list (list): The original list to modify.
        idx (int): The index at which to replace the element.
        element (any): The new element to insert into the list.

    Returns:
        list: A new list with the element replaced if the index is valid;
              otherwise, a copy of the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return list(my_list)
    
    # Create a copy of the original list
    new_list = list(my_list)
    new_list[idx] = element
    
    return new_list
