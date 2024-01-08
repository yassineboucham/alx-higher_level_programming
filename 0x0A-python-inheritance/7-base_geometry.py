#!/usr/bin/python3
"""task 7"""


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
