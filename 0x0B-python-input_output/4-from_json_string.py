#!/usr/bin/python3
""" Module 4-from_json_string.
function that returns an object (Python data structure)
represented by a JSON string.
"""
import json


def from_json_string(my_obj):
    """ returns an object represented by JSON string
    Args:
        my_obj: JSON string
    Returns:
        an object represented by a JSON string
    """

    return json.loads(my_obj)
