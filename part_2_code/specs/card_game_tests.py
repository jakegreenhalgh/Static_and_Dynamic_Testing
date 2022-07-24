import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.spades = Card("Spades", 1)
        self.hearts = Card("Hearts", 11)
        self.clubs = Card("Clubs", 7)
        self.diamonds = Card("Diamonds", 4)

    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.spades))
