import unittest

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('John', 'Doe')
        
    def test_name_property(self):
        self.assertEqual(self.person.first_name, 'John')
        self.assertEqual(self.person.last_name, 'Doe')
