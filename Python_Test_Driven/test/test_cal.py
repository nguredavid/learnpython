#!/usr/bin/python3

import unittest

'''create a class'''
class Tdd(unittest.Testcase):

    '''create a method'''
    def test_calc_method(self):
        calc = Calculation()
        result = calc.add(2,2)
        self.assertEqual(4, result)

'''to run the script in the standard way'''
if __name__ == '__main__':
    unittest.main()
