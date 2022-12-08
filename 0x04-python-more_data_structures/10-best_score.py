#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        lists = []
        for i in a_dictionary.values():
            lists.append(i)
        for j in a_dictionary:
            if a_dictionary[j] == max(lists):
                return j
