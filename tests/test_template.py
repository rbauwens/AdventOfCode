import unittest
from days.template import template_function

class AddTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(5, template_function(5))


