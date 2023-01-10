#!/usr/bin/python3
""" Module 2-append_write
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ appends a string to a text file
    Args:
        filename: file to append text to
        text: string to append to filename
    Returns:
        number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        numOf_char = f.write(text)
    return numOf_char
