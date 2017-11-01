import unittest
from card import Card

class TestCard(unittest.TestCase):
    def test_comparisons(self):
        self.assertTrue(Card('A', 'h') > Card('K', 's'))
        self.assertEqual(Card('A', 'h'), Card('A', 'd'))
        self.assertTrue(Card('7', 'd') < Card('J', 'c'))
        self.assertTrue(Card('K', 's') >= Card('J', 'c'))
