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
