#!/usr/bin/python3
""" Module 6-load_from_json_file.
function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ creates an object from json file
    Args:
        filename: json file
    Returns:
        object in the json file
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        obj = f.read()
    return json.loads(obj)
