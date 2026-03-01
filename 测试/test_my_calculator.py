import unittest
from 核心.my_calculator import my_adder

class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(2,3), 5)

    def test_negative_with_negative(self):
        self.assertEqual(my_adder(-2,3), 1)