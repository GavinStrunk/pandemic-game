from dataclasses import dataclass

@dataclass
class Player:
    location: str

class Researcher(Player):
    """
    You may give any 1 of your City cards when you Share Knowledge. It need not mathc your city. A player who Shares Knowledge with you on their turn can take any 1 of your City cards.
    """
    name: str


class Scientist():
    """
    You need only 4 cards of the same color to do the Discover a Cure action.
    """
    name: str


class ContingencyPlanner():
    """
    As an action, take any discarded Event card and store it on this card.
    When you play the stored Event card, remove it from the game.
    Limit: 1 Event card on this card at a time, which is not part of your hand
    """
    name: str


class OperationsExpert:
    """
    As an action, build a research station in the city you are in (no City card needed).
    Once per turn as an action, move from a research station to any city by discarding any City card.
    """
    name: str


class QuarantineSpecialist:
    """
    Prevent disease cube placements (and outbreaks) in the city you are in and all cities connected to it.
    """
    name: str


class Medic:
    """
    Remove all cubes of one color when doing Treat Disease.
    Automatically remove cubes of cured diseases from the city you are in (and prevent them from being placed there).
    """
    name: str


class Dispatcher:
    """
    Move another player's pawn as if it were yours.
    As an action, move any pawn to a city with another pawn.
    Get permission before moving another player's pawn.
    """
    name: str
