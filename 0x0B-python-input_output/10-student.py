#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dicti = self.__dict__.copy()
        attr_ret = {}
        if type(attrs) is list:
            if not all(isinstance(i, str) for i in attrs):
                return dicti
                
            else:
                for i in dicti:
                    if i in attrs:
                        attr_ret[i] = i
                return attr_ret
        return dicti
