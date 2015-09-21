'''
Game has Rules
Game has Players
Player has Hand
'''
class Card(object):
    
    def __init__(self, card_value_suit):
        self.value = card_value_suit[0]
        self.suit = card_value_suit[1]
        
class Cards(object):
    
    def __init__(self):
        self.values = [str(i) for i in range(2,10)]
        self.values += ['T', 'J', 'Q', 'K', 'A']
        self.suits = ['C', 'D', 'H', 'S']
        self.build_dicts()
        
    def build_dicts(self):
        self.value_dict = {}
        self.suit_dict = {}
        for value in self.values:
            self.value_dict[value] = 0
        for suit in self.suits:
            self.suit_dict[suit] = 0
    
class Hand(Cards):
    
    def __init__(self, card_codes):
        self.card_codes = card_codes
        self.read_cards()
    
    def read_cards(self):
        cards = self.card_codes.split(' ')
        self.cards = []
        self.dictionary = Cards()
        
        for card in cards:
            self.cards.append(Card(card))            
        
        for card in self.cards:
            v = card.value
            s = card.suit
            self.dictionary.value_dict[v]+=1
            self.dictionary.suit_dict[s]+=1
            
        print self.dictionary.value_dict
        print self.dictionary.suit_dict
        
        print 'max(self.dictionary.value_dict.values())', max(self.dictionary.value_dict.values())
        print 'max(self.dictionary.suit_dict.values())', max(self.dictionary.suit_dict.values())
        
        # need to finish... just figured this would be more laborious than challenging
        

class Poker(object):
    
    
    hands = [
        ['High Card', 'high_card',  'Highest value card.'],
        ['One Pair', 'one_pair', 'Two cards of the same value.'],
        ['Two Pairs', 'two_pairs', 'Two different pairs.'],
        ['Three of a Kind', 'three_of_a_kind', 'Three cards of the same value.'],
        ['Straight', 'straight', 'All cards are consecutive values.'],
        ['Flush', 'flush' 'All cards of the same suit.'],
        ['Full House', 'full_house', 'Three of a kind and a pair.'],
        ['Four of a Kind', 'four_of_a_kind', 'Four cards of the same value.'],
        ['Straight Flush', 'striaght_flush', 'All cards are consecutive values of same suit.'],
        ['Royal Flush', 'royal_flush', 'Ten, Jack, Queen, King, Ace, in same suit.']
    ]

    def __init__(self, hand):
        self.hand = hand
        self.cards = Cards()
        self.read_hand()
    
    def read_hand(self):
        pass
    
    

c = Cards()
print 'all cards:', c.values
h = Hand('5H 5C 6S 7S KD')
# print h.cards
