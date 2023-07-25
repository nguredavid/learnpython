#!/usr/bin/python3
import unittest

from app.hudson import adds

class test_sums(unittest.TestCase):
    def test_result(self):
        result = adds(2, 5)
        self.assertEqual(result, 7)

