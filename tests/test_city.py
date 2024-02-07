#!/usr/bin/python3
"""city unittest"""

import unittest
from models.city import City


class TestBase(unittest.TestCase):
    """testing City"""

    def test_set(self):
        self.C = City()

