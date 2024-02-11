#!/usr/bin/python3
"""Amenity"""

import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test the module"""

    def test_Set(self):
        """create an instance"""
        self.A = Amenity()

    def test_Exist(self):
        """check if attributes exist"""
        Amenity1 = Amenity()
        self.assertTrue(hasattr(Amenity1, "id"))
        self.assertTrue(hasattr(Amenity1, "created_at"))
        self.assertTrue(hasattr(Amenity1, "updated_at"))
        self.assertTrue(hasattr(Amenity1, "name"))

    def test_User(self):
        """check if values are correct type"""
        Amenity2 = Amenity()
        self.assertIsInstance(Amenity2.id, str)
        self.assertIsInstance(Amenity2.created_at, datetime)
        self.assertIsInstance(Amenity2.updated_at,datetime)
        self.assertIsInstance(Amenity2.name, str)
