#!/usr/bin/python3
# Author - Awogbemila Tobi

def uppercase(str):
    """Print a string in uppercase."""
    for alphabet in str:
        if ord(alphabet) in range(97, 123):
            alphabet = chr(ord(alphabet) - 32)
            print(alphabet, end='')
        else:
            print(alphabet, end='')

