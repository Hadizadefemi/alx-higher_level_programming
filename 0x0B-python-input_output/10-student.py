#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dicti = {}
        if type(attrs) == list:
            if all(isinstance(i, str) for i in attrs):
                for i in attrs:
                    if i in self.__dict__.copy():
                        dicti[i] = self.__dict__.copy()[i]
                return dicti
        else:
            return self.__dict__.copy()
