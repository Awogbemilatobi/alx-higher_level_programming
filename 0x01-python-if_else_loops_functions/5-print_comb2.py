#!/usr/bin/python3
"""a program that prints numbers from 0 to 99"""

for number in range(0, 100):
    if number == 99:
        print(f"{number:02}", end="")
    else:
        print(f"{number:02}, ", end="")
print()
