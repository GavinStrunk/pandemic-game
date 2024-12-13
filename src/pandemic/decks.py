import torch
from pandemic.cards import Card
from typing import List

class Deck:
    """
    A Deck is a collection of Cards and consists of a draw pile and a discard pile. Cards can also be removed from the Deck which effectively removes them entirely from the game.

    Args:

    """
    def __init__(self,
                 cards: torch.tensor,
                 device: str = 'cpu'
                 ):
        self.cards = cards

    def shuffle(self):
        pass

    def draw_card(self):
        pass

    def add_card(self, card):
        pass

class InfectionDeck(Deck):
    def __init__(self, cards):
        super().__init__(cards)

class PlayerDeck(Deck):
    def __init__(self, cards):
        super().__init__(cards)