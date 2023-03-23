#!/usr/bin/python3
"""Author Awogbemila Tobi
a function that returns a tuple with the length of a string and its first character."""


def multiple_returns(sentence):

    if sentence == "":
        sentence[:1] = None
    else:
        new_tuple = (len(sentence), sentence[:1])
    return new_tuple


