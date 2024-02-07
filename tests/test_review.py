#!/usr/bin/python3
"""unittest Review"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """testing Review"""

    def test_review(self):
        self.assertIsInstance(Review().place_id, str)
        self.assertIsInstance(Review().user_id, str)
        self.assertIsInstance(Review().text, str)
