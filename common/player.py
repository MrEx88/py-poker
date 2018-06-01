
class Player():
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = None
        
        
    def bet(self, bet):
        actual_bet = money
        if bet < money:
            money -= bet
            actual_bet = bet
        else:
            money = 0
        return actual_bet
        
        
    def can_bet(self, minimum_bet):
        return money >= minimum_bet
        
        
    def fold(self):
        self.cards = None
        
        
    def check(self):
        pass
        
        
    def set_cards(self, cards):
        self.cards = cards
