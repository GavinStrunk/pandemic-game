"""
# Pandemic Board Game


"""
import functools

import numpy as np
from gymnasium import spaces
from pettingzoo import AECEnv
from typing import Optional, List, Union

from pettingzoo.utils.env import AgentID, ObsType


def env(**kwargs):
    env = PandemicGame(**kwargs)
    return env


class PandemicGame(AECEnv):
    r"""
    Pandemic Board Game

    """
    metadata = {
        "name": "pandemic_game_v0",
        "render_modes": ["human", "rgb_array"],
    }
    def __init__(self,
                 players: Union[List[str] | int],
                 render_mode: Optional[str]
                 ):
        super(PandemicGame, self).__init__()
        self.render_mode = render_mode
        # Number of players and the type
        self.players = players
        self.num_players = len(players)
        assert 2 <= self.num_players <= 4, "Must have between 2 and 4 players"

        # Difficulty of the game: i.e. number of infection cards

        # Game State variables
        self.outbreaks = 0
        self.cures = np.zeros(4)
        self.infection_rate = 0

    @functools.lru_cache(maxsize=None)
    def action_space(self, agent) -> spaces.Space:
        """

        """

        return spaces.Discrete(3)

    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        return spaces.Box()

    def reset(
        self,
        seed: int | None = None,
        options: dict | None = None,
    ) -> None:
        # Setup Game
        # Place research station in Atlanta
        self.outbreaks = 0
        self.cures = np.zeros(4)
        self.infection_rate = 0
        # Shuffle infection cards
        # Flip over 3 infection cards and place 3 disease cubes of the matching color
        # Flip over 3 more cards and place 2 disease cubes
        # Flip over 3 more cards and place 1 disease cube
        # Place all 9 cards face up in the infection deck discard pile
        # Random choose players unless they are provided
        # Place all players in Atlanta
        # Shuffle player deck without epidemic cards
        # Deal players initial hands
        self.num_player_cards = 4 - (self.num_players - 2)

        # Create epidemic cards based on difficulte: easy - 4, medium - 5, hard - 6
        # Divide player deck into equal parts with the number of epidemic cards
        # Shuffle 1 epidemic card into each pile and combine

        pass

    def observe(self, agent: AgentID) -> ObsType | None:
        return None

    def step(self, agent: AgentID) -> ObsType | None:
        # Do 4 actions
        # Draw 2 player cards
        # Infect cities
        pass
