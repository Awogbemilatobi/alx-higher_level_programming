#!/usr/bin/python3
# Author - Awogbemila Tobi

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:]) #prints first n characters and last n+1 characters, this skipping n
