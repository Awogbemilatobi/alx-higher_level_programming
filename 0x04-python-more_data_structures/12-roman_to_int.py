#!/usr/bin/python3
"""Awogbemila Tobi
 a function def roman_to_int(roman_string): that
 converts a Roman numeral to an integer."""
 
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
 
def roman_to_int(str):
    res = 0
    i = 0
 
    for i in range(len(str)):
        s1 = value(str[i])   # Getting value of symbol s[i]
        if (i + 1 < len(str)):            
            s2 = value(str[i + 1]) # Getting value of symbol s[i + 1]
            
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res
 
