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
