#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        dicti = self.__dict__.copy()
        attr_ret = {}
        if type(attr) is list:
            if all(isinstance(i, str) for i in attr):
                for i in attr:
                    for j in dicti:
                        if i == j:
                            attr_ret[i] = dicti[i]
                return attr_ret
        else:
            return dicti
