from .card import *

HAND_TOTAL = 5

def get_winning_hands(hands):
    "Returns a list of winning hands: poker([hand, ...]) => [hand, ...]"
    return __allmax(hands, key=hand_rank)
    
def __allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    highestHandRank = hand_rank(max(iterable, key=key))
    winners = []
    for itr in iterable:
        if hand_rank(itr) == highestHandRank:
            winners.append(itr)
            
    return winners
    
    
def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand) 
    if is_straight(ranks) and is_flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif is_flush(hand):
        return (5, ranks)
    elif is_straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif is_two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
        
        
def card_ranks(hand):
    "Returns a list of the ranks, sorted with the higher first."
    ranks = [('--' + ALL_RANKS).index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks
    
    
def best_five(hand):
    "Takes a hand and gives the best 5 cards."
    return max(itertools.combinations(hand, HAND_TOTAL), key=hand_rank)
    
    
def is_straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks) - min(ranks)) == 4  and len(set(ranks)) == HAND_TOTAL
    
    
def is_flush(hand):
    "Return True if all the cards have the same suit."
    return all([hand[0][1] == h[1] for h in hand])
    
    
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    try:
        return next(r for r in ranks if ranks.count(r) == n)
    except:
        return None
        
        
def is_two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
        
        