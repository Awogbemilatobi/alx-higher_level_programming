#!/usr/bin/python3
#Author: Awogbemila Tobi
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w", encoding = "utf-8"):
        filename = json.dumps(my_obj)
