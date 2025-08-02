# cardstuff.py
# YOUR NAME AND NETID HERE;
# PUT THE DATE HERE
# skeleton by L. Lee, S. Marschner, W. White


""" Functions dealing with Cards as defined by module card_labv1
"""
import random


# Helper for draw_poker_hand
def draw(deck):
    """Returns: a single Card that is randomly drawn (and removed) from deck.

    Precondition: deck is a list of Cards containing at least one Card."""
    card = random.choice(deck)
    deck.remove(card)
    return card
      # STUDENTS: finish this implementation



# Helper for class Card and thus, indirectly, for sorting in draw_poker_hand.
# Placed in this file so students need only edit one file.
def less_than(c1, c2):
    """Returns:
       True if either:
        * the rank of Card c1 is less than the rank of c2, or
        * c1 has the same rank as c2 but a suit that is less than c2's suit
       Returns False otherwise.

    Precondition: c1 and c2 are Cards."""

    rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suit_order = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    if c1.rank < c2.rank:
        return True
    elif c1.rank == c2.rank:
        if c1.suit < c2.suit:
            return True

    return False
     # STUDENTS: finish this implementation


def draw_poker_hand(deck):
    """Returns: list of five Cards drawn from deck, in reverse sorted order.
    The drawn Cards are removed from deck.

    Precondition: deck is a list of Cards containing at least five Cards."""

    hand = []

    for _ in range(5):
        card = draw(deck)
        hand.append(card)

    hand.sort(reverse=True)


    return hand
      #STUDENTS: implement this function using a for-loop
