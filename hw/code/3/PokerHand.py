"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import division
from pprint import pprint
from Card import *


labels = ['straightflush','fourofakind','fullhouse','flush','straight','threeofakind','twopair', 'pair']
class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        self.rank = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.rank[card.rank] = self.rank.get(card.rank, 0) + 1
        self.rankList = self.rank.values()
        self.rankList.sort(reverse=True)
    
    def has_straight(self):
        """Checks whether this hand has a straight."""
        # make a copy of the rank histogram before we mess with it
        rankList = self.rank.copy()
        rankList[14] = rankList.get(1, 0)
        # see if we have 5 in a row
        return self.in_a_row(rankList)
    
    def in_a_row(self, rankList):
        """Checks whether the list has 5 ranks in a row.

        rankList: rank of List of the cards under consideration
        """
        count = 0
        for i in range(1, 15):
            if rankList.get(i, 0):
                count += 1
                if count == 5: return True
            else:
                count = 0
        return False
    
    def check_rank(self,*args):
        """Checks for cards in the same rank.
        args : Number of cards of the same rank of interest
        """
        for i,j in zip(args,self.rankList):
            if i>j:
                return False
        return True

    def has_straightflush(self):
        """Checks for straight flush
           
           rankList: rank of List of the cards under consideration
        """
        for suit in range(0,4):
            rankList = {}
            for card in self.cards:
                if(suit==card.suit):
                    rankList[card.rank] = 1
                    if card.rank == 1:
                        rankList[14] = 1
            if len(rankList)==0:continue
            if (self.in_a_row(rankList)):
                return True
        return False
        
    def classify(self):
        self.suit_hist()
        for l in labels:
            _ = getattr(self,'has_'+l)
            if _():
                #print l
                return l
    
    def has_fourofakind(self):
        """Returns True if the hand has 4 cards of the same rank, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.check_rank(4)
    
    def has_fullhouse(self):
        """Returns True if the hand has a full house, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.check_rank(3,2)
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_threeofakind(self):
        """Returns True if the hand has 3 cards of the same rank, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.check_rank(3)
        
    def has_twopair(self):
        """Returns True if the hand has 2 pairs, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.check_rank(2,2)
    
    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.check_rank(2)

def handLabeling(s,cards):
    deck = Deck()
    deck.shuffle()
    handLabel = []
    # deal the cards and classify the hands
    for i in range(s):
        hand = PokerHand()
        deck.move_cards(hand, cards)
        hand.sort()
        handLabel.append(hand.classify())
    return handLabel

def probability(n=1000,s=7,cards=7):
    count = {}
    for i in range(0,n):
        inhand = handLabeling(s,cards)
        for l in inhand:
            count[l] = count.get(l,0) + 1
    tot = s * 1000
    print "Total count of each label\n"
    print count
    print "\n"
    print "Probability of each label\n"
    for l in labels:
        count[l] = count.get(l,0)/tot
        pprint(l+ ":" +"%.5f" %count[l]) 
    
if __name__ == '__main__':
    numofIter = 1000
    sizeofHand = 7
    cards = 7
    probability(numofIter,sizeofHand,cards)
    # make a deck
    