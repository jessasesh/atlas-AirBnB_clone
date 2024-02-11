#!/usr/bin/python3
"""state unittests"""

import unittest
from datetime import datetime
from models.state import State



class TestState(unittest.TestCase):
    """testing state"""

    def test_Set(self):
        """creates attribute"""
        self.S = State()

    def test_Exist(self):
        """if attributes exist"""
        State1 = State()
        self.assertTrue(hasattr(State1, "id"))
        self.assertTrue(hasattr(State1, "created_at"))
        self.assertTrue(hasattr(State1, "updated_at"))
        self.assertTrue(hasattr(State1, "name"))

    def test_User(self):
        """if values are correct"""
        State2 = State()
        self.assertIsInstance(State2.id, str)
        self.assertIsInstance(State2.created_at, datetime)
        self.assertIsInstance(State2.updated_at, datetime)
        self.assertIsInstance(State2.name, str)