#!/usr/bin/python3
def square_matrix_map(my_list=[]):
    return (list(map(lambda lista: list(map(lambda x: x * x, lista)), matrix)))
