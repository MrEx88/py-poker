import random # this will be a useful library for shuffling


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
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks
    
    
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    return (max(ranks) - min(ranks)) == 4  and len(set(ranks)) == 5
    
def flush(hand):
    "Return True if all the cards have the same suit."
    return all([hand[0][1] == h[1] for h in hand])
    
    
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    try:
        return next(r for r in ranks if ranks.count(r) == n)
    except:
        return None
        
        
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    pairs = []
    for r in ranks:
        if ranks.count(r) == n: 
            pairs.append(r) 
    return tuple(pairs) if len(pairs) == 2 else None
    
    
def test():
    sf = "6C 7C 8C 9C TC".split()
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = " 9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
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
    print(poker([sf, sf2, fk, fh]))
    assert poker([sf, sf2, fk, fh]) == [sf, sf2] 
    return "tests pass"
    
    
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC'] ):
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