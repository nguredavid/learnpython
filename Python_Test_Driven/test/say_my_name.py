#!/usr/bin/python3

import unittest
from app.my_name import say_my_name

class Test_iMy_names(unittest.TestCase):

    def test_case_name(self):
        result = say_my_name("David", "Ngure")
        
        self.assertEqual(result, "Names: David Ngure")
