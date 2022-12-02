#!/usr/bin/python3
def element_at(mylist, idx):
    if (idx < 0) or (idx >= len(mylist)):
        return None
    else:
        for i in range(len(mylist)):
            if i == idx:
                return mylist[i]
