#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    else:
        set_a = set()
        for i in my_list:
            set_a.add(i)

    return sum(set_a)
