import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = []
        self._initialize_deck()

    def _initialize_deck(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        # equal to below:
        # for suit in suits:
        #   for rank in ranks:
        #     deck.append(Card(rank, suit))
        
    def __str__(self):
        return f"{self.deck}"

    def shuffle(self):
        random.shuffle(self.deck)

    
def main():

    random.shuffle(deck)
    for card in deck:
        print(card)

if __name__ == "__main__":
    main()
