#!/usr/bin/python3
""" Module 5-save_to_json_file
function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a JSON file
    Args:
        my_obj: object
        filename: json file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
