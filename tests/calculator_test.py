import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):


    def test_calculator_can_add(self):
        self.assertEqual(2,add_two_numbers(1,1))

    def test_calculator_can_subtract(self):
        self.assertEqual(1,subtract_two_numbers(2,1))