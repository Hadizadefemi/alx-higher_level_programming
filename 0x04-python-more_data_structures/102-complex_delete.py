#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        y = {}
	for k, v in a_dictionary.items():
            if v != value:
                y[k] = v
        a_dictionary = y.copy()
    return a_dictionary
