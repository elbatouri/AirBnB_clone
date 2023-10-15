#!/usr/bin/python3
"""imports modules to test amenity class"""

import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """class that is set to unittest amenity"""

    def test_do_module(self):
        """tests the length of amenity.__doc__"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """test Amenity doc constructor"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)
    def test_class(self):
        """tests amnenity class attr & inheritance from basemodel"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))
        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)
if __name__ == '__main__':
    unittest.main()
