#!/usr/bin/python3
#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using '#'."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += "#"
            rec += "\n"
        return rec.rstrip()

    def __repr__(self) -> str:
        """return self.__width, self.height"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.height)

    def __del__(self):
        """print the mesge after delite"""
        print("Bye rectangle...")
