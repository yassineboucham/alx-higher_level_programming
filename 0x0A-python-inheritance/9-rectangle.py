#!/usr/bin/python3
"""task 8"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """str"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """w * h"""
        return (self.__width * self.__height)
