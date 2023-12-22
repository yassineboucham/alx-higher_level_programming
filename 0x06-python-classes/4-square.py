#!/usr/bin/python3
"""Squer module."""


class Square():
    """Defines a square."""

    def size(self, value):
        """setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def size(self):
        """getter"""
        return self.__size

    def __init__(self, size=0):
            self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
