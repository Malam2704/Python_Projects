import random

class Card:
    # have attributes for t,he class to use to make the card
    suits = ["SP", "HE", "DI", "CL"]
    rank = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self, rank, suit=None):
        if(rank == "JOKER"):
            self.rank = "JOKER"
            self.suit = None
        else:
            self.rank = rank
            self.suit = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"