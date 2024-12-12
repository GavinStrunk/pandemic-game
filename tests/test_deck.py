import pytest
from pandemic_game.deck import Card, Deck, deck_from_cities, initialize_player_deck, shuffle_deck, draw_card, add_card, \
    combine_decks  # Replace 'your_module' with the actual name of your module


def test_deck_from_cities():
    cities = {'cities': [["San Francisco", "blue"], ["Chicago", "blue"]]}
    deck = deck_from_cities(cities)
    assert len(deck.cards) == len(cities)
    for card in deck.cards:
        assert card.name in dict(cities).keys()
        assert card.color in dict(cities).values()


def test_initialize_player_deck():
    player_deck = Deck(cards=[Card(card_type="City", name="City1"), Card(card_type="City", name="City2")])
    epidemic_cards = [Card(card_type="Epidemic")]
    initialized_deck = initialize_player_deck(player_deck, epidemic_cards)
    assert len(initialized_deck.cards) == len(player_deck.cards) + len(epidemic_cards)

    with pytest.raises(ValueError):
        initialize_player_deck(player_deck, [])


def test_shuffle_deck():
    deck = Deck(cards=[Card(card_type="City", name=f"City{i}") for i in range(5)])
    shuffled_deck = shuffle_deck(deck)
    assert len(shuffled_deck.cards) == len(deck.cards)
    assert set(card.name for card in shuffled_deck.cards) == set(card.name for card in deck.cards)


def test_draw_card():
    deck = Deck(cards=[Card(card_type="City", name=f"City{i}") for i in range(5)])
    new_deck, card = draw_card(deck)
    assert card in deck.cards
    assert len(new_deck.cards) == len(deck.cards) - 1

    with pytest.raises(ValueError):
        draw_card(Deck(cards=[]))


def test_add_card():
    deck = Deck(cards=[Card(card_type="City", name="City1")])
    new_card = Card(card_type="City", name="City2")
    new_deck = add_card(deck, new_card)
    assert len(new_deck.cards) == len(deck.cards) + 1
    assert new_card in new_deck.cards


def test_combine_decks():
    deck1 = Deck(cards=[Card(card_type="City", name="City1")])
    deck2 = Deck(cards=[Card(card_type="City", name="City2")])
    combined_deck = combine_decks(deck1, deck2)
    assert len(combined_deck.cards) == len(deck1.cards) + len(deck2.cards)
    assert set(card.name for card in combined_deck.cards) == {"City1", "City2"}
