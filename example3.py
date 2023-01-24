import unittest

class TestStringMethods(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
