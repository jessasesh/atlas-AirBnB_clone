#!/usr/bin/python3
"""User unittest"""

import unittest
from models.user import User


class TestBase(unittest.TestCase):
    """testing user"""

    def test_Set(self):
        self.U = User()