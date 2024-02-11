#!/usr/bin/python3
"""city unittest"""

import unittest
from datetime import datetime
from models.city import City


class TestBase(unittest.TestCase):
    """testing City"""

    def test_Set(self):
        """generate instance"""
        self.C = City()

    def test_Exist(self):
        """if attributes exists"""
        City1 = City()
        self.assertTrue(hasattr(City1, "state_id"))
        self.assertTrue(hasattr(City1, "name"))

    def test_User(self):
        City2 = City()
        self.assertIsInstance(City2.state_id, str)
        self.assertIsInstance(City2.name, str)