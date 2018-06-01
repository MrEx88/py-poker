from common import holdem, card
import itertools
import unittest


class Hands(unittest.TestCase):
    def setUp(self):
        self.straight_flush = ("6%s 7%s 8%s 9%s T%s" % tuple(itertools.repeat(card.CLUB, holdem.HAND_TOTAL))).split()
        self.straight_flush2 = ("6%s 7%s 8%s 9%s T%s" % tuple(itertools.repeat(card.DIAMOND, holdem.HAND_TOTAL))).split() # Straight Flush
        self.four_of_kind = ("9%s 9%s 9%s 9%s 7%s" % (card.DIAMOND, card.HEART, card.SPADE, card.CLUB, card.DIAMOND)).split()
        self.full_house = ("T%s T%s T%s 7%s 7%s" % (card.DIAMOND, card.CLUB, card.HEART, card.CLUB, card.DIAMOND)).split()
        self.two_pair = ("5%s 5%s 9%s 9%s 6%s" % (card.SPADE, card.DIAMOND, card.HEART, card.CLUB, card.SPADE)).split() # Two pairs
        
        
    def test_kind(self):
        self.four_of_kindranks = holdem.card_ranks(self.four_of_kind)
        tpranks = holdem.card_ranks(self.two_pair)
        self.assertEqual(holdem.kind(4, self.four_of_kindranks), 9)
        self.assertEqual(holdem.kind(3, self.four_of_kindranks), None)
        self.assertEqual(holdem.kind(2, self.four_of_kindranks), None)
        self.assertEqual(holdem.kind(1, self.four_of_kindranks), 7)
        
        
    def test_straight(self):
        self.assertEqual(holdem.is_straight([9, 8, 7, 6, 5]), True)
        self.assertEqual(holdem.is_straight([9, 8, 8, 6, 5]), False)
        
        
    def test_flush(self):
        self.assertEqual(holdem.is_flush(self.straight_flush), True)
        self.assertEqual(holdem.is_flush(self.four_of_kind), False)
        
        
    def test_poker(self):
        self.assertEqual(holdem.get_winning_hands([self.straight_flush, self.four_of_kind, self.full_house]), [self.straight_flush])
        self.assertEqual(holdem.get_winning_hands([self.four_of_kind, self.full_house]), [self.four_of_kind])
        self.assertEqual(holdem.get_winning_hands([self.full_house, self.full_house]), [self.full_house, self.full_house])
        self.assertEqual(holdem.get_winning_hands([self.straight_flush]), [self.straight_flush])
        self.assertEqual(holdem.get_winning_hands([self.straight_flush] + 99*[self.full_house]), [self.straight_flush])
        self.assertEqual(holdem.get_winning_hands([self.straight_flush, self.straight_flush2, self.four_of_kind, self.full_house]), [self.straight_flush, self.straight_flush2])
        
       
def run():
    unittest.main()
    
    
if __name__ == '__main__':
    run() #unittest.main()

