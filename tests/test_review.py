#!/usr/bin/python3
"""unittest Review"""

import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """testing Review"""

    def test_Set(self):
        """creates instance"""
        self.R = Review()

    def test_Exist(self):
        """if attributes exist"""
        Review1 = Review()
        self.assertTrue(hasattr(Review1, "id"))
        self.assertTrue(hasattr(Review1, "created_at"))
        self.assertTrue(hasattr(Review1, "updated_at"))
        self.assertTrue(hasattr(Review1, "place_id"))
        self.assertTrue(hasattr(Review1, "user_id"))
        self.assertTrue(hasattr(Review1, "text"))

    def test_User(self):
        """if values are correct type"""
        Review2 = Review()
        self.assertIsInstance(Review2.id, str)
        self.assertIsInstance(Review2.created_at, datetime)
        self.assertIsInstance(Review2.updated_at, datetime)
        self.assertIsInstance(Review2.place_id, str)
        self.assertIsInstance(Review2.user_id, str)
        self.assertIsInstance(Review2.text, str)
