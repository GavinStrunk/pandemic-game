"""
Defines the different decks of cards that are present in the game.
"""
import random
from dataclasses import dataclass
from abc import abstractmethod
from typing import List, Tuple, Optional


@dataclass(frozen=True)
class Card:
    card_type: str
    name: Optional[str] = None
    color: Optional[str] = None

    @property
    @abstractmethod
    def type(self):
        pass

"""
Event Cards
One Quiet Night: Skip the next infect cities step (Do not flip over any infection cards).
Resiliant Population: Remove any 1 card in the infection discard pile from the game. You may play this between the infect and intensify steps of an epidemic.
Airlift: Move any 1 pawn to any city. Get permission before moving another player's pawn.
Forecast: Draw, look at, and rearrange the top 6 cards of the infection deck. Put them back on top.
Government Grant: Add 1 research station to any city (No city card needed).
"""
@dataclass(frozen=True)
class Deck:
    cards: List[Card]


def deck_from_cities(cities: dict) -> Deck:
    # Create City cards
    city_cards = []
    for city in cities['cities']:
        city_cards.append(Card(name=city[0], color=city[1]))

    return Deck(cards=city_cards)


def initialize_player_deck(player_deck: Deck, epidemic_cards: List[Card]) -> Deck:
    if len(epidemic_cards) == 0:
        raise ValueError("There must be at least one epidemic card")

    split_size = len(player_deck.cards) // len(epidemic_cards)
    split_decks = []

    # Split the deck into parts and add an epidemic card to each part
    for i in range(0, len(epidemic_cards)):
        if i < len(epidemic_cards) - 1:
            # Regular split for all but the last epidemic card
            part = player_deck.cards[i * split_size:(i + 1) * split_size]
        else:
            # The last part takes the remaining cards
            part = player_deck.cards[i * split_size:]

        part.append(epidemic_cards[i])
        random.shuffle(part)
        split_decks.append(part)

    # Combine the shuffled parts back together
    combined_cards = [card for split_deck in split_decks for card in split_deck]
    return Deck(cards=combined_cards)


def shuffle_deck(deck: Deck) -> Deck:
    shuffled_cards = random.sample(deck.cards, len(deck.cards))
    return Deck(cards=shuffled_cards)


def draw_card(deck: Deck, from_bottom: bool = False) -> Tuple[Deck, Card]:
    if not deck.cards:
        raise ValueError("Cannot draw from an empty deck")

    if from_bottom:
        # Draw from the bottom of the deck
        drawn_card = deck.cards[0]
        new_deck = Deck(cards=deck.cards[1:])
    else:
        # Draw from the top of the deck
        drawn_card = deck.cards[-1]
        new_deck = Deck(cards=deck.cards[:-1])

    return new_deck, drawn_card


def add_card(deck: Deck, card: Card) -> Deck:
    return Deck(cards=deck.cards + [card])


def combine_decks(deck1: Deck, deck2: Deck):
    combined_cards = deck1.cards + deck2.cards
    return Deck(cards=combined_cards)
