#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    last = number % 10
    print(last, end="")
    return last