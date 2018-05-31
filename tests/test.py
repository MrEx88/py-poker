import sys
sys.path.append("..")
from poker import *
import itertools
import unittest


class Hands(unittest.TestCase):
    def setUp(self):
        self.straight_flush = ("6%s 7%s 8%s 9%s T%s" % tuple(itertools.repeat(CLUB, 5))).split()
        self.straight_flush2 = ("6%s 7%s 8%s 9%s T%s" % tuple(itertools.repeat(DIAMOND, 5))).split() # Straight Flush
        self.four_of_kind = ("9%s 9%s 9%s 9%s 7%s" % (DIAMOND, HEART, SPADE, CLUB, DIAMOND)).split()
        self.full_house = ("T%s T%s T%s 7%s 7%s" % (DIAMOND, CLUB, HEART, CLUB, DIAMOND)).split()
        self.two_pair = ("5%s 5%s 9%s 9%s 6%s" % (SPADE, DIAMOND, HEART, CLUB, SPADE)).split() # Two pairs
        
        
    def test_kind(self):
        self.four_of_kindranks = card_ranks(self.four_of_kind)
        tpranks = card_ranks(self.two_pair)
        self.assertEqual(kind(4, self.four_of_kindranks), 9)
        self.assertEqual(kind(3, self.four_of_kindranks), None)
        self.assertEqual(kind(2, self.four_of_kindranks), None)
        self.assertEqual(kind(1, self.four_of_kindranks), 7)
        
        
    def test_straight(self):
        self.assertEqual(straight([9, 8, 7, 6, 5]), True)
        self.assertEqual(straight([9, 8, 8, 6, 5]), False)
        
        
    def test_flush(self):
        self.assertEqual(flush(self.straight_flush), True)
        self.assertEqual(flush(self.four_of_kind), False)
        
        
    def test_poker(self):
        self.assertEqual(poker([self.straight_flush, self.four_of_kind, self.full_house]), [self.straight_flush])
        self.assertEqual(poker([self.four_of_kind, self.full_house]), [self.four_of_kind])
        self.assertEqual(poker([self.full_house, self.full_house]), [self.full_house, self.full_house])
        self.assertEqual(poker([self.straight_flush]), [self.straight_flush])
        self.assertEqual(poker([self.straight_flush] + 99*[self.full_house]), [self.straight_flush])
        self.assertEqual(poker([self.straight_flush, self.straight_flush2, self.four_of_kind, self.full_house]), [self.straight_flush, self.straight_flush2])
        
        
if __name__ == '__main__':
    unittest.main()

