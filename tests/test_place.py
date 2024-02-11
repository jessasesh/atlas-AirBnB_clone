#!/usr/bin/python3
"""Place Unittest"""

import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing place"""

    def test_Set(self):
        """create instance"""
        self.P = Place()

    def test_Exist(self):
        """attribute exists"""
        Place1 = Place()
        self.assertTrue(hasattr(Place1, "id"))
        self.assertTrue(hasattr(Place1, "created_at"))
        self.assertTrue(hasattr(Place1, "city_id"))
        self.assertTrue(hasattr(Place1, "user_id"))
        self.assertTrue(hasattr(Place1, "name"))
        self.assertTrue(hasattr(Place1, "description"))
        self.assertTrue(hasattr(Place1, "number_rooms"))
        self.assertTrue(hasattr(Place1, "number_bathrooms"))
        self.assertTrue(hasattr(Place1, "max_guest"))
        self.assertTrue(hasattr(Place1, "price_by_night"))
        self.assertTrue(hasattr(Place1, "latitude"))
        self.assertTrue(hasattr(Place1, "longitude"))
        self.assertTrue(hasattr(Place1, "amenity_ids"))

    def test_User(self):
        """if values are correct"""
        Place2 = Place()
        self.assertIsInstance(Place2.id, str)
        self.assertIsInstance(Place2.created_at, datetime)
        self.assertIsInstance(Place2.updated_at,datetime)
        self.assertIsInstance(Place2.city_id, str)
        self.assertIsInstance(Place2.user_id, str)
        self.assertIsInstance(Place2.name, str)
        self.assertIsInstance(Place2.description, str)
        self.assertIsInstance(Place2.number_rooms, str)
        self.assertIsInstance(Place2.number_bathrooms, int)
        self.assertIsInstance(Place2.max_guest, int)
        self.assertIsInstance(Place2.price_by_night, int)
        self.assertIsInstance(Place2.latitude, float)
        self.assertIsInstance(Place2.longitude, float)
        self.assertIsInstance(Place2.amenity_ids, list)