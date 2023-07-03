#!/usr/bin/python3

import unittest

from app.adds_integer import add_integer

class test_add(unittest.TestCase):

    def test_adding(self):
        result = add_integer(2, 5)
        self.assertEqual(7, result)

