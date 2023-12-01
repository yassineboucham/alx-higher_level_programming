#!/usr/bin/python3
def uppercase(str):
    up = ""
    for char in str:
        if ('a' <= char <= 'z'):
            up += chr(ord(char) - 32)
        else:
            up += char
    print(up)