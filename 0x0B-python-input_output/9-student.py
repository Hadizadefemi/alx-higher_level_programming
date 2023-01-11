#!/usr/bin/python3
""" Module 9-student
class that defines a Student
"""


class Student:
    """ student identified by name and age"""

    def __init__(self, first_name, last_name, age):
        """ Inits Student with theirs names and age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation of an instance
        """
        dictionary = {}
        dictionary = self.__dict__.copy()
        return dictionary
