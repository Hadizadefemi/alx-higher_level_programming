#!/usr/bin/python3
""" Module 0-read_file.
defines a functuon that reads a text file
and prints in stdout
"""


def read_file(filename=""):
    """prints content of the text file to stdout
    Args:
        filename: the file to read
    """

    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
