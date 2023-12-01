#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        last_degit = number % 10
    else:
        last_degit = (number * -1) % 10
    print("{}".format(last_degit), end="")
    return (last_degit)
