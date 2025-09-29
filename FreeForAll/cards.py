class Card:
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        if(suit in self.suits):
            self.suit = suit
        else:
            self.suit = None

        if(rank in self.ranks):
            self.rank = rank
        else:
            self.rank = None

    def __str__(self):
        return f"{self.suit} {self.rank}"

def check_flush():
    
def main():
    real_card = Card("hearts","A")
    fake_card = Card('bars',"F")
    print(real_card, fake_card)

main()