#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that replaces an element in a list at a specific position
without modifying the original list"""

def new_in_list(my_list, idx, element):
    new_list = []

    if idx < 0 or idx > len(my_list):
        return  my_list
    else:
        for elements in my_list:
            new_list.append(elements)
        new_list[idx] = element
    return new_list
