import unittest

class TestStringMethods(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(int(''), None)
        self.assertEqual(int(' '), None)
