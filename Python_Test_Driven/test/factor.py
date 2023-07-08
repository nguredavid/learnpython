#!/usr/bin/python3

import unittest

from app.factorial import factorial

class Test_fact(unittest.TestCase):

    def test_factorial(self):
        res = factorial(3)
        self.assertEqual(6, res)
