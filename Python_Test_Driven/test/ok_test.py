#!/usr/bin/python3

import unittest

from app.ok import add_integer

class Test_add(unittest.TestCase):
    def test_fxn(self):
        result = add_integer("k", 3.05)
        self.assertEqual(101.05, result)
    
