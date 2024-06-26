#!/usr/bin/python3
def print_square(size):
    """function that prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is int and size < 0:
        raise ValueError("size must be an integer")
    j = 0
    i = 0
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print('')
if __name__ == "__main__":
    import doctest
    doctest.testfile("4-print_square.txt")
