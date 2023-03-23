#!/usr/bin/python3
# Author - Awogbemila Tobi
"""a program that prints the ASCII alphabet, in reverse order, alternating lowercase 
and uppercase (z in lowercase and Y in uppercase), not followed by a new line

for alphabets in reversed(range(97, 123)):
    if alphabets%2 == 1:
        print(f"{chr(alphabets-32)}", end='')
    else:
        print(f"{chr(alphabets)}", end='')
