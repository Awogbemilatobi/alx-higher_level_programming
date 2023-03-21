#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that returns elements taht appears only once in the two sets"""

def only_diff_elements(set_1, set_2):
    set_3 = set_1.symmetric_difference(set_2)
    return set_3

