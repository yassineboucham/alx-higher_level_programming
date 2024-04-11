#!/usr/bin/python3

def add_integer(a, b=98):
    """
    add tow numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
