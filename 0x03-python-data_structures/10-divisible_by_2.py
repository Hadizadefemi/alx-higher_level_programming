#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    else:
        new_list = []
        for i in my_list:
            if (i % 2) == 0:
                i = True
            else:
                i = False
            new_list.append(i)
    return new_list
