from dataclasses import dataclass

import pandemic_game.deck
import pandemic_game.io
import pandemic_game.world

@dataclass
class GameState:
    world: pandemic_game.world.World
    infection_deck: pandemic_game.deck.Deck
    infection_discard: pandemic_game.deck.Deck
    player_deck: pandemic_game.deck.Deck
    player_discard: pandemic_game.deck.Deck
    infection_rate: int
    num_outbreaks: int
    num_research_stations: int
    num_blue_cubes: int
    num_red_cubes: int
    num_yellow_cubes: int
    num_black_cubes: int
    blue_disease_state: str
    red_disease_state: str
    yellow_disease_state: str
    black_disease_state: str



@dataclass
class GameConfig:
    cities_file: str
    seed: int
    difficulty: int
    players: dict


def initialize_game() -> GameState:
    cities_file = '../config/cities.yaml'
    cities_data = pandemic_game.io.load_cities(cities_file)

    # Initialize the world
    world = pandemic_game.world.create_world(cities_data=cities_data)

    # Initialize decks based on difficulty
    infection_deck = pandemic_game.deck.deck_from_cities(cities=cities_data)
    infection_discard = pandemic_game.deck.Deck(cards=[])
    player_deck = pandemic_game.deck.deck_from_cities(cities=cities_data)
    player_discard = pandemic_game.deck.Deck(cards=[])

    player_deck = pandemic_game.deck.initialize_player_deck(player_deck=player_deck)

    # Initialize players
    # Initialize players hands
    # Start all players in Atlanta
    # Set a research center in Atlanta

    # Set order of players. The player with highest population card goes first.

    # Infect initial cities

    game = GameState(
        world=world,
        infection_deck=infection_deck,
        infection_discard=infection_discard,
        player_deck=player_deck,
        player_discard=player_discard,
        infection_rate=2,
        num_outbreaks=0,
        num_research_stations=6,
        num_blue_cubes=24,
        num_red_cubes=24,
        num_yellow_cubes=24,
        num_black_cubes=24,
        blue_disease_state='viral',
        red_disease_state='viral',
        yellow_disease_state='viral',
        black_disease_state='viral'
    )
    return game


def play_turn(game: GameState):
    # Do 4 actions
    # Draw 2 player cards
    # If epidemic card comes up handle that
    # Enforce 7 card handle limit
    # Infect cities
    pass


def check_if_game_over(game_state: GameState) -> int:
    """
    The game is not over:
    * 0
    The game ends in a win if:
    * 1: all 4 diseases are cured or eradicated
    The game ends in a lose if:
    * 2: number of outbreaks reaches 8
    * 3: unable to place the number of disease cubes (ran out)
    * 4: player cannot draw 2 cards after doing an action (ran out)
    Args:
        game_state:

    Returns:

    """
    return 0
