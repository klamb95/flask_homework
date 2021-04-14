import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):


    def test_calculator_can_add(self):
        self.assertEqual(2,add_two_numbers(1,1))

    def test_calculator_can_subtract(self):
        self.assertEqual(1,subtract_two_numbers(2,1))

    def test_calculator_can_multiply(self):
        self.assertEqual(10, multiply_two_numbers(2,5))

    def test_calculator_can_divide(self):
        self.assertEqual(5, divide_two_numbers(10,2))