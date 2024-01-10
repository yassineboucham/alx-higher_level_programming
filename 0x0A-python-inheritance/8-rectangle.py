#!/usr/bin/python3
"""task 8"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """ raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("7-base_geometry.txt")

class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
