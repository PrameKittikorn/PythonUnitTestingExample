import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_multiple_calls(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(5, 6), 11)
