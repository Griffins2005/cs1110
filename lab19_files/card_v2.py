"""
A module providing a class for playing cards

This implementation is adapted from chapter 18 of _Think Python_, 2ed, 
by Allen B. Downey.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Version:  Mar 25, 2025 - removes @classmethod, use dictionaries rank & suit storage
"""
from functools import total_ordering  # for implementing comparisons in Python3

# translations of valid int ranks to names
SUIT_NAMES = {0:'Clubs', 1:'Diamonds', 2:'Hearts', 3:'Spades'}

# translations of one-char suit codes to suit ints
SUIT_ENCODE={}
for (s_int, s_name) in SUIT_NAMES.items():
    SUIT_ENCODE[s_name[0]] = s_int

# translations of valid int ranks to names
RANK_NAMES = {1:'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7',
              8:'8', 9:'9', 10:'Ten', 11:'Jack', 12:'Queen', 13:'King'}

# translations of one-char rank codes to rank ints
RANK_ENCODE={}
for (r_int, r_name) in RANK_NAMES.items():
    RANK_ENCODE[r_name[0]] = r_int


# decorator "fills in" missing comparisons, at the cost of speed
@total_ordering
class Card:
    """
    A class to represent playing cards.
    
    """
    ### HIDDEN INSTANCE ATTRIBUTES
    # Attribute _suit: the suit of this particular card.
    # Invariant: _suit is an int (key) in  SUIT_NAMES
    #
    # Attribute _rank: the rank of this particular card.
    # Invariant: _rank is an int (key) in RANK_NAMES

    def getSuit(self):
        """
        Returns the suit of this card as an int.
    
        0 means clubs, 1 means diamonds, 2 means hearts, 3 means spades
        """
        return self._suit

    def setSuit(self,value):
        """
        Sets the suit of this card.

        The suit is an int (key) in SUIT_NAMES.

        Parameter value: The new suit value
        Precondition: value is an int in SUIT_NAMES
        """
        assert isinstance(value, int), 'suit %s is not an int' % repr(value)
        assert value in SUIT_NAMES, 'suit %d is out of range' % value
        self._suit = value

    def getRank(self):
        """
        Returns the rank of this card, as an int.

        The rank refers to the card value where 'Ace' is 1, 'Jack' is 11,
        'Queen' is 12, and 'King' is 13. 
        """
        return self._rank

    def setRank(self,value):
        """
        Sets the rank of this card.

        The rank refers to the card value where 'Ace' is 1, 'Jack' is 11,
        'Queen' is 12, and 'King' is 13.

        Parameter value: The new rank value
        Precondition: value is an int (key) in RANK_NAMES
        """
        assert isinstance(value, int), 'rank %s is not an int' % repr(value)
        assert value in RANK_NAMES, 'rank %d is out of range' % value
        self._rank = value

    # This is a DERIVED attribute (it is a combination of suit and rank)
    def getCode(self):
        """
        Returns a two-character code for the card.

        The code is a two-character string whose first character represents
        the rank and the second is the first initial of the suit.  Non-number
        ranks are represented by initials.  So '3H' stands for 3 of hearts,
        and 'KS' stands  for king of spades).  We use 'T' for Ten.
        """
        # Get the initial letters from SUIT_NAMES
        suit = SUIT_NAMES[self._suit][0]
        rank = RANK_NAMES[self._rank][0]
        return rank+suit

    def setCode(self, code):
        """
        Sets the rank and suit of this card using a two-character code.

        The code should be a two-character string whose first character
        represents the rank and the second is the first initial of the suit.
        Non-number ranks are represented by initials.  So '3H' stands for
        3 of hearts, and 'KS' stands for king of spades).  We use 'T'
        for Ten.

        Parameter code: The code for the new rank and suit
        Precondition: code is a 2-char string, value[0] in 'A23456789TJQK'
        and value[1] in 'CDHS'.
        """
        assert isinstance(code, str), 'code %s is not a str' % repr(code)
        assert len(code) == 2, 'code %s has the incorrect length' % repr(code)
        assert code[0] in RANK_ENCODE, 'rank %s is invalid' % repr(code[0])
        assert code[1] in SUIT_ENCODE, 'suit %s is invalid' % repr(code[1])

        self._rank=RANK_ENCODE[code[0]]
        self._suit=SUIT_ENCODE[code[1]]

    def __init__(self, suit=0, rank=1, code=None):
        """
        Initializes a card with the given suit and rank.
        
        The suits and rank are represented as integers. Alternatively,
        suit and rank can be encoded together in a two-character string like
        '3H' (3 of hearts) or 'KS' (king of spades).  We use 'T' for Ten.
        
        The possible suits are given as values in SUIT_NAMES, while 
        the possible ranks are given as values in RANK_NAMES.  
        
        Example: if we execute c = Card(0, 12), then this card is the Queen of
        Clubs, since SUIT_NAMES[0] is 'Clubs' and RANK_NAMES[12] is 'Queen'. 
        The same card could be created by Card(code='QC').
        
        If the code parameter is used, the suit and rank parameters are ignored.
        
        Parameter suit: the suit encoding (optional)
        Precondition: suit is an int (key) in SUIT_NAMES (inclusive)
        
        Parameter rank: the rank encoding (optional)
        Precondition: rank is an int (key) in RANK_NAMES
        
        Parameter code: the card encoded as a string (optional)
        Precondition: code is a 2-char string with code[0] in 'A23456789TJQK'
        and code[1] in 'CDHS'.
        """
        # The setters take care of all the asserts
        if code is not None:
            self.setCode(code)          
        else:
            self._rank = rank
            self._suit = suit
    
    def __str__(self):
        """
        Returns a readable string representation of this card.
        
        Examples: '2 of Hearts'
                  'Ten of Clubs'
        """
        return RANK_NAMES[self._rank] + ' of ' + SUIT_NAMES[self._suit]

    def __repr__(self):
        """Returns: Unambiguous string representation of this card that can be
        used to create a copy.
        Example: 'Card(3,2)'
        """
        return f'Card({self._suit}, {self._rank})'

    
    def __eq__(self, other):
        """Returns: 
        NotImplemented if `other` is not a Card.
        Otherwise, returns...
            True if `other` is a Card that has the same suit and rank 
            as this Card;
            False otherwise. """
        if not isinstance(other, Card):
            return NotImplemented
        else:
            return self._suit == other._suit and self._rank == other._rank

    def __lt__(self, other):
        """
        Returns: True if this card is less than other
        
        Cards are compared according to poker ordering, with Aces high.
        
        Parameter other: the value to compare
        Precondition: other is a Card
        """
        if (self._rank == other._rank):
            return self._suit < other._suit
        else:

            if RANK_NAMES[self._rank] != 'Ace':
                left = self._rank
            else:
                left = max(RANK_NAMES.keys())+1  # largest possible number

            if RANK_NAMES[other._rank] != 'Ace':
                rght = other._rank
            else:
                rght = max(RANK_NAMES.keys())+1 

            return left < rght

    def __hash__(self):
        """Returns a so-called 'hash' of this object, which is necessary to
        allow Cards to be items in sets.  We make the 'hash' of a Card
        be a tuple of its suit and rank.
        """
        # In Python 3, if you override __eq__, __hash__ will be set to None
        # unless __hash__ is defined
        return hash((self._suit, self._rank))


def full_deck():
    """
    Returns the list of the standard 52 cards.
    """
    output = []  # list of cards so far to be returned
    for suit in range(len(SUIT_NAMES)):
        for rank in RANK_NAMES: 
            output.append(Card(suit,rank))
    return output


def list_str(clist):
    """Returns: human_friendly string (no newlines) representing the
    items in `clist`.
    Precondition: clist is a (possibly empty) list."""
    return '['+', '.join(map(str, clist))+']'


