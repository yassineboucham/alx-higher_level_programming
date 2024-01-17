#!/usr/bin/python3
"""

square


"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
            )

    @property
    def size(self):
        """get size"""
        return self.height

    @size.setter
    def size(self, value):
        """set value"""
        super().validation("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary """
        dic = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            }
        return dic
