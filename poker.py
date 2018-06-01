# Make sure to specify the utf-8 encoding (because of the suits) when reading from the REPL. 
#   exec(open("<filepath>\\poker.py", encoding="utf-8").read())

import itertools
import random



def best_wild_hand(hand):
    "Trys all values for jokers in all 5-card selections."
    hand = set(best_hand(h)
               for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)
    
    
def replacements(card):
    """Returns a list of the possible replacements for a card.
    There will be more than 1 only for wild cards."""
    if card == '?B': return ALL_BLACK_CARDS
    elif card == '?R': return ALL_RED_CARDS
    else: return [card]
    
    
def deal(numhands):
    deck = list(ALL_CARDS)
    hands = []
    random.shuffle(deck)
    for k in range(numhands):
        hand = []
        for i in range(HAND_TOTAL):
            num = random.randint(0, len(deck)-1)
            hand.append(deck.pop(num))
        hands.append(hand)
        
    return hands
    
print(deal(2))