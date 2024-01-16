#!/usr/bin/python3
""" Module that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.validation("width", width)
        self.__width = width
        self.validation("height", height)
        self.__height = height
        self.validation("x", x)
        self.__x = x
        self.validation("y", y)
        self.__y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter width"""
        self.validation("width", width)
        self.__width = width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter height"""
        self.validation("height", height)
        self.__height = height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter x"""
        self.validation("x", x)
        self.__x = x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter y"""
        self.validation("y", y)
        self.__y = y

    def validation(self, attr_name, attr_value):
        """validation"""
        if not isinstance(attr_value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if attr_name in ("width", "height"):
            if attr_value <= 0:
                raise ValueError("{} must be > 0".format(attr_name))
        elif attr_name in ("x", "y"):
            if attr_value < 0:
                raise ValueError("{} must be >= 0".format(attr_name))

    def area(self):
        """area"""
        return self.__height * self.__width

    def display(self):
        """display"""
        j = 0
        while j < self.__height:
            i = 0
            while i < self.__width:
                i += 1
                print("#", end="")
            j += 1
            print("")

    def __str__(self):
        """str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            )

    def display(self):
        """display"""
        y = 0
        while y < self.__y:
            print("")
            y += 1
        height = 0
        while height < self.__height:
            x = 0
            width = 0
            while x < self.__x:
                print(" ", end='')
                x += 1
            while width < self.__width:
                print("#", end='')
                width += 1
            print("")
            height += 1

    def update(self, *args, **kwargs):
        """update"""
        if args:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)
