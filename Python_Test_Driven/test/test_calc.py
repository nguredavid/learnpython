#!/usr/bin/python3

import unittest
from app.calcs import Calc
class test_calc(unittest.TestCase):

    def test_mod(self):
        calc = Calc()
        result = calc.adds(3,2)
        self.assertEqual(5, result)

