"""
A module providing a class for Cripple Mr. Onion cards, i.e.,
with eight suits: spades, hearts, diamonds, clubs plus staves, cups, coins,
and swords.

Author: Lillian Lee (LJL2)
Version: Apr 27, 2025
"""
import card_v2 as cfile


# Translations of valid int ranks to names
SUIT_NAMES = cfile.SUIT_NAMES  # A trick: modifying SUIT_NAMES now also modifies
                               # cfile.SUIT_NAMES, so we can update it in 
                               # cfile.SUIT_NAMES in the next line
SUIT_NAMES.update({4: 'sTaves', 5: 'cOins', 6: 'cUps', 7: 'sWords'})
# The methods in card_v2.Card refer to cfile.SUIT_NAMES, which we've now altered
# to suit (ha) our purposes.

# Translations of one-char suit codes to suit ints.
# For the new suits, we use the second letter of the name
SUIT_ENCODE=cfile.SUIT_ENCODE # Same trick as above
SUIT_ENCODE.update({'T': 4, 'O': 5, 'U': 6, 'W': 7})

# Translations of valid int ranks to names, such as 1 to "Ace" or 13 to "King"
RANK_NAMES = cfile.RANK_NAMES

# Translations of one-char rank codes to rank ints
RANK_ENCODE = cfile.RANK_ENCODE


class OnionCard(cfile.Card):
    """Represents a Cripple Mr. Onion (CMO) card.

    OnionCards have the usual ranks (1..13 = Ace .. King) but they have extra suits.
    In the listing below, the capitalized letter is the one-letter code for that
    suit.
    Clubs
    Diamonds
    Hearts
    Spade
    sTaves
    cOins
    cUps
    sWords
    """

    ### HIDDEN INSTANCE ATTRIBUTES
    # Attribute _suit: the suit of this particular card.
    # Invariant: _suit is an int (key) in  SUIT_NAMES
    #
    # Attribute _rank: the rank of this particular card.
    # Invariant: _rank is an int (key) in RANK_NAMES
    pass

    def __init__(self, s=0, r=1, code=None):
        """Initializes an OnionCard with the given suit and rank.
        
        Raises an OnionError if code is not None.
        """
        if code is not None:
            raise OnionError("OnionCards can't be initialized by codes")

    def getCode(self):
        """
        Raises an OnionError, since we aren't allowing codes for OnionCards
        """
        raise OnionError("OnionCards don't have associated codes, due to ambiguity")

    def setCode(self, code):
        """
        Raises an OnionError, since we aren't letting
        OnionCards to be specified by codes.
        """
        raise OnionError("OnionCards don'")
       

def full_deck():
    """
    Returns the list of the 104 cards.
    """
    output = []  # list of cards so far to be returned
    for suit in range(len(SUIT_NAMES)):
        for rank in RANK_NAMES: 
            output.append(OnionCard(suit,rank))
    return output


class OnionError(Exception):
    """
    Exception class for errors with OnionCards.
    """
    pass


