#!/usr/bin/python3
"""Author: Awogbemila Tobi
a function that removes all characters c and C from a string"""

def no_c(my_string):
   
    new_string = ""
    for alphabets in my_string:
        if alphabets == "c" or alphabets == "C":
            continue
        new_string = new_string + alphabets
    return new_string
