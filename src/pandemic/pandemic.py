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
        # Difficulty of the game: i.e. number of infection cards

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
        pass

    def observe(self, agent: AgentID) -> ObsType | None:
        return None

    def step(self, agent: AgentID) -> ObsType | None:
        pass

    def state(self) -> np.ndarray:
        pass
