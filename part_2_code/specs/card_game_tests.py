import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.spades = Card("Spades", 1)
        self.hearts = Card("Hearts", 11)
        self.clubs = Card("Clubs", 7)
        self.diamonds = Card("Diamonds", 4)
        self.cards = [self.spades, self.hearts, self.clubs, self.diamonds]

    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.spades))

    def test_highest_card(self):
        self.assertEqual(self.clubs, CardGame.highest_card(self, self.clubs, self.diamonds))

    def test_cards_total(self):
        self.assertEqual("You have a total of 23", CardGame.cards_total(self, self.cards))