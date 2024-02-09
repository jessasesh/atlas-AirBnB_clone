#!/usr/bin/python3
"""Place Unittest"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing place"""

    def test_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)