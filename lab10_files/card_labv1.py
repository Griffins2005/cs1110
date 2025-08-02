# card_labv1.py
# Lillian Lee, Steve Marschner, and Walker White
# Mar 2025

"""  Module for standard playing cards (no jokers).

Defines the class Card and provides a few Card-related functions.

Implementation adapted from chapter 18 of the second edition of the course text, _Think Python_,
by Allen B. Downey.

Students will need to correctly implement a function in cardstuff.py for Card
comparison (specifically, the _lt_ method in class Card) for this
code to work correctly.
"""

from functools import total_ordering  # for implementing comparisons in Python3
import cardstuff

# SUIT_NAME[0] is 'Clubs', SUIT_NAME[1] is 'Diamonds', etc.
SUIT_NAME = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
NUM_SUITS = len(SUIT_NAME)

# First item is None so that RANK_NAME[1] is 'Ace', RANK_NAME[2] is '2', etc.
RANK_NAME = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King']
NUM_RANKS = len(RANK_NAME)-1


# This @-statement "fills in" unwritten comparisons such as __gt__,
# at the cost of speed
@total_ordering
class Card():
    """An instance is a standard playing card (no jokers).

    Instance Attributes:
      suit [int in 0..NUM_SUITS-1]: this Card's suit
      rank [int in 1..NUM_RANKS]: this Card's rank

    Example:  A Card with suit 0 and rank 12 would be the Queen of Clubs, since
    SUIT_NAME[0] is 'Clubs' and RANK_NAME[12] is 'Queen'.
    """

    def __init__(self, s, r):
        """Initializer: A new Card with suit s and rank r.

        Example: if we execute
            c = Card(3, 1)
        then this card is the Ace of Spades, since SUIT_NAME[3] is 'Spades' and
        RANK_NAME[1] is 'Ace'.

        Preconditions: s is an int in 0..NUM_SUITS-1
                       r is an int in 1..NUM_RANKS
        """
        self.suit = s
        self.rank = r

    def __str__(self):
        """Returns: Readable string representation of this Card.
        Example: '2 of Hearts'
        """
        return RANK_NAME[self.rank] + ' of ' + SUIT_NAME[self.suit]

    def __repr__(self):
        """Returns: Unambiguous string representation of this card.
        Example: 'Card(3,2): 2 of Spades'
        """
        outstring = 'Card'
        outstring += '(' + str(self.suit) + ',' + str(self.rank) + ')'
        outstring += ': ' + str(self)
        return outstring

    # We've included __eq__ so that we can do testing of equality of cards and
    # lists of cards.
    def __eq__(self, other):
        """Returns: Truth value of the statement:
             `other` is a Card with same suit and rank as this Card
        *except*: returns NotImplemented if `other` is not a Card."""
        if not isinstance(other, Card):
            return NotImplemented
        else:
            return (self.suit, self.rank) == (other.suit, other.rank)

    def __lt__(self, other):
        """Returns:
        True if `other` is a Card and either:
            * the rank of this Card is less than the rank of `other`, or
            * this Card has the same rank as `other` but a suit that is less
                than the suit of `other`;
        False if `other` is a Card and neither *'d condition above holds;
        NotImplemented if `other` is not a Card"""
        if not isinstance(other, Card):
            return NotImplemented
        else:
            # Students will implement less_than
            return cardstuff.less_than(self, other)


def full_suit(s):
    """
    Returns a list of the 13 cards of suit s in ascending rank.

    s: an int in 0..NUM_SUITS-1
    """
    output = []
    for rank in range(1, NUM_RANKS+1):
        # range(1,n) creates the list [1,2,...,n-1],
        # Thus, we skip the None entry at the beginning
        output.append(Card(s, rank))
    return output


def full_deck():
    """Returns: list of the standard 52 Cards, sorted by ascending suit then
        ascending rank: Ace of Clubs first, King of Spades last."""
    output = []  # list of cards so far to be returned
    for suit in range(NUM_SUITS):
        # range(n) creates the range [0,1,2,...,n-1]
        output.extend(full_suit(suit))
    return output


def print_cards(clist):
    """Print cards in clist as a human-readable sequence of lines.

    Precondition: clist is a (possibly empty) list of Cards."""
    for c in clist:
        print(c)


def print_cards2(clist):
    """Altered implementation of print_cards just for lab purposes"""
    for c in clist:
        print("c")


def print_cards3(clist):
    """Altered implementation of print_cards just for lab purposes"""
    for i in range(len(clist)):
        print(clist[i])


def print_cards_condensed(clist):
    """Print cards in clist as a human-readable single line.

    Precondition: clist is a (possibly empty) list of Cards.."""
    for c in clist:
        # Use semi-colons for separators instead of newlines
        print(c, end='; ')
    print()
