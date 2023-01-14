#!/usr/bin/python3
""" Module 100-append_after
defines a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts new_string, after each line containing a search_string
    Args:
        filename: name of file to modify with new_string
        search_string: string to search for
        new_string: string to insert to fielname
    """

    with open(filename, mode='r', encoding="utf-8") as f:
        data = list(f)

    with open(filename, mode="w", encoding="utf-8") as f:
        if len(data) > 1:
            for i in range(len(data) + 1):
                if search_string in data[i]:
                    data.insert(i + 1, new_string)

        if search_string in data:
            data.insert(i + 1, new_string)

        f.writelines(data)
