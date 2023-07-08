#!/usr/bin/python3

import unittest

from app.print_square import prints_square

class test_prt(unittest.TestCase):

    def test_print_sq(self):

        result = prints_square(-1)
        self.assesrtEqual:(result, ''*5)

