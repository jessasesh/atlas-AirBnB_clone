#!/usr/bin/python3
"""User unittest"""

import unittest
from datetime import datetime
from models.user import User


class TestBase(unittest.TestCase):
    """testing user"""

    def test_Set(self):
        """creates instance"""
        self.U = User()

    def test_Exist(self):
        """if attributes exist"""
        User1 = User()
        self.assertTrue(hasattr(User1, "id"))
        self.assertTrue(hasattr(User1, "created_at"))
        self.assertTrue(hasattr(User1, "updated_at"))
        self.assertTrue(hasattr(User1, "email"))
        self.assertTrue(hasattr(User1, "password"))
        self.assertTrue(hasattr(User1, "first_name"))
        self.assertTrue(hasattr(User1, "last_name"))

    def test_User(self):
        """if values area correct"""
        User2 = User()
        self.assertIsInstance(User2.id, str)
        self.assertIsInstance(User2.created_at, datetime)
        self.assertIsInstance(User2.updated_at, datetime)
        self.assertIsInstance(User2.email, str)
        self.assertIsInstance(User2.password, str)
        self.assertIsInstance(User2.first_name, str)
        self.assertIsInstance(User2.last_name, str)