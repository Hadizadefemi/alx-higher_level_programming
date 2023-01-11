#!/usr/bin/python3
""" Module 8-class_to_json
function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""


def class_to_json(obj):
    """ returns dictionary description of an object
    Args:
        obj: instance of a class
    Returns:
        dictionary description of the obj
    """
    dictionary = {}

    if hasattr(obj, "__dict__"):
        dictionary = obj.__dict__.copy()

    return dictionary
