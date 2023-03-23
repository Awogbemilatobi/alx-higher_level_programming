#!/usr/bin/python3
"""Awogbemila Tobi
 a function that returns a new dictionary with all values multiplied by 2"""

def multiply_by_2(a_dictionary):
    squared_dict = a_dictionary.copy()

    for value in squared_dict.keys():
        squared_dict[value] = squared_dict[value]*2
    return squared_dict

