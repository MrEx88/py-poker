# Make sure to specify the utf-8 encoding (because of the suits) when reading from the REPL. 
#   exec(open("<filepath>\\poker.py", encoding="utf-8").read())

import itertools
import random

HEART   = '♥' # Alt+3
DIAMOND = '♦' # Alt+4
CLUB    = '♣' # Alt+5
SPADE   = '♠' # Alt+6
ALL_RANKS = '23456789TJQKA'
ALL_SUITS = HEART + DIAMOND + CLUB + SPADE
ONE_DECK = [r+s for r in ALL_RANKS for s in ALL_SUITS]
ALL_RED_CARDS = [rs for rs in ONE_DECK if DIAMOND in rs or HEART in rs]
ALL_BLACK_CARDS = [rs for rs in ONE_DECK if SPADE in rs or CLUB in rs]

def poker(hands):
    "Returns a list of winning hands: poker([hand, ...]) => [hand, ...]"
    return allmax(hands, key=hand_rank)
    
def allmax(iterable, key=None):
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
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
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
    return max(itertools.combinations(hand, 5), key=hand_rank)
    
    
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks) - min(ranks)) == 4  and len(set(ranks)) == 5
    
def flush(hand):
    "Return True if all the cards have the same suit."
    return all([hand[0][1] == h[1] for h in hand])
    
    
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    try:
        return next(r for r in ranks if ranks.count(r) == n)
    except:
        return None
        
        
def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
        
        
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
    
    
def test():
    sf = ("6%s 7%s 8%s 9%s T%s" % tuple(itertools.repeat(CLUB, 5))).split()
    sf2 = ("6%s 7%s 8%s 9%s T%s" % tuple(itertools.repeat(DIAMOND, 5))).split() # Straight Flush
    fk = ("9%s 9%s 9%s 9%s 7%s" % (DIAMOND, HEART, SPADE, CLUB, DIAMOND)).split()
    fh = ("T%s T%s T%s 7%s 7%s" % (DIAMOND, CLUB, HEART, CLUB, DIAMOND)).split()
    tp = ("5%s 5%s 9%s 9%s 6%s" % (SPADE, DIAMOND, HEART, CLUB, SPADE)).split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert poker([sf, sf2, fk, fh]) == [sf, sf2] 
    return "tests pass"
    
    
def test_best_five():
    assert sorted(best_five(("6%s 7%s 8%s 9%s T%s 5%s J%s" % (CLUB, CLUB, CLUB, CLUB, CLUB, CLUB, SPADE)).split())) \
        == ['6'+CLUB, '7'+CLUB, '8'+CLUB, '9'+CLUB, 'T'+CLUB]
    assert sorted(best_five(("T%s T%s T%s 7%s 7%s 8%s 8%s" % (HEART, CLUB, DIAMOND, CLUB, DIAMOND, CLUB, SPADE)).split())) \
        == ['8'+SPADE, '8'+CLUB, 'T'+CLUB, 'T'+HEART, 'T'+DIAMOND]
    assert sorted(best_five(("T%s T%s T%s 7%s 7%s 7%s 7%s" % (DIAMOND, CLUB, SPADE, CLUB, DIAMOND, SPADE, HEART)).split())) \
        == ['7'+SPADE, '7'+CLUB, '7'+HEART, '7'+DIAMOND, 'T'+DIAMOND]
    return "test_best_five passes"
    
    
ONE_DECK = [r+s for r in ALL_RANKS for s in ALL_SUITS]

def deal(numhands, n=5, deck=ONE_DECK):
    hands = []
    random.shuffle(deck)
    for k in range(numhands):
        hand = []
        for i in range(n):
            num = random.randint(0, len(deck)-1)
            hand.append(deck.pop(num))
        hands.append(hand)
        
    return hands
    
print(deal(2))
print(test())
print(test_best_five())