#!/usr/bin/python3
"""

base


"""
from models.base import Base
import unittest


class TesrBaseMethods(unittest.TestCase):
    """test Base Method"""

    def test_id(self):
        """test id"""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_assigned(self):
        """assigned """
        new = Base(44)
        self.assertEqual(new.id, 44)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)
