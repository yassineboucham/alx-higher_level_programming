#!/usr/bin/python3
"""Squer module."""


class Square():
    """Defines a square."""
    
    def __init__(self, size=0):
        """intalise"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def size(self, value):
        """setter """
        self.__size = value

    def size(self):
        """getter"""
        return self.__size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
