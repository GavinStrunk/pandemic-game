from dataclasses import dataclass
from enum import Enum

class CardType(Enum):
    """
    The types of cards that are in the game.
    """
    CITY = 0
    EVENT = 1
    INFECTION = 2

class CardColor(Enum):
    BLUE = 0
    RED = 1
    BLACK = 2
    YELLOW = 3
    GREEN = 4

@dataclass
class Card:
    """
    Card object that represents a card in the game.

    Parameters:
        card_type (CardType): The type of card.
        name (str): Either the city name or the card name.
        color (str): The color associated with the section colors in the game. Non-city cards have color green.
    """
    card_type: CardType
    name: str
    color: CardColor