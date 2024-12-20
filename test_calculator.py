# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_abs_add(self):
        self.assertEqual(self.calc.abs_add(2, -3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        pass # teste faltando

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)