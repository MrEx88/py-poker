
HEART   = '♥' # Alt+3
DIAMOND = '♦' # Alt+4
CLUB    = '♣' # Alt+5
SPADE   = '♠' # Alt+6
ALL_RANKS = '23456789TJQKA'
ALL_SUITS = HEART + DIAMOND + CLUB + SPADE

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = rank+suit
        
        
ALL_CARDS = [Card(r, s) for r in ALL_RANKS for s in ALL_SUITS]
ALL_RED_CARDS = [card for card in ALL_CARDS if DIAMOND in card.value or HEART in card.value]
ALL_BLACK_CARDS = [card for card in ALL_CARDS if SPADE in card.value or CLUB in card.value]
