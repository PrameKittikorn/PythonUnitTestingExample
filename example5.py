import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
