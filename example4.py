import unittest

class TestStringMethods(unittest.TestCase):
    def test_input_types(self):
        self.assertEqual(int('1'), 1)
        self.assertEqual(int(1), 1)
