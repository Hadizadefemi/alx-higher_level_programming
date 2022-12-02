#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    else:
        modified_list = my_list[:]
        for i in range(len(modified_list)):
            if i == idx:
                modified_list[i] = element
    return modified_list
