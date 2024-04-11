#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char in ('.', '?', ':'):
            print('\n')
        else:  
            print(char, end='')
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
