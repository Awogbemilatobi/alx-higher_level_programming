#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that prints a dictionary by ordered keys."""

def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(key, value)
