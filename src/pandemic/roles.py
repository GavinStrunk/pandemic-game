import torch


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def drive(self):
        pass

    def direct_flight(self):
        pass

    def charter_flight(self):
        pass

    def shuttle_flight(self):
        pass

    def build_research_station(self):
        pass

    def treat_disease(self):
        pass

    def share_knowledge(self):
        pass

    def discover_cure(self):
        pass

class Researcher(Player):
    """
    Researcher may give any 1 of their City cards when they Share Knowledge. It need not match their city.
    """
    def __init__(self, name, location):
        super().__init__(name, location)
