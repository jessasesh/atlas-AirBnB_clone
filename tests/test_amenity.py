#!/usr/bin/python3
"""Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """test the module"""

    def test_class(self):
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))