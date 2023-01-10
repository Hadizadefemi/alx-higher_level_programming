#!/usr/bin/python3
""" Module 1-write_file.
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ writes a string to a text file
    Args:
        filename: file to write to
        text: text to write to the file
    Returns:
        number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        numOf_char = f.write(text)
    return numOf_char
