# cardstufftest.py
# Lillian Lee (LJL2) and Steve Marschner (SRM2)
# Mar 2022

"""Module for testing some functions in cardstuff"""

import cornellasserts
import card_labv1  # need to create Cards for test cases
import cardstuff
import sys




def test_draw():
    """Quick diagnostic test of whether cardstuff.draw seems to be working.
    May depend on equality being correct for cards"""
    print("Running test_draw")

    # Create a 1-card deck with just the Jack of Diamonds, so draw()'s results
    # are completely predictable.
    deck1 = [card_labv1.Card(1,11)]
    c = cardstuff.draw(deck1)
    cornellasserts.assert_equals(0, len(deck1))  # deck1 should be empty
    cornellasserts.assert_equals(card_labv1.Card, type(c))
    cornellasserts.assert_equals(1, c.suit)
    cornellasserts.assert_equals(11, c.rank)

    # Now trying to draw from a full deck, checking that we don't seem to
    # be drawing from the same position each time
    orig_deck = card_labv1.full_deck()
    clist = card_labv1.full_deck()
    c1 = cardstuff.draw(clist)
    i1 = orig_deck.index(c1)
    orig_deck.pop(i1)
    c2 = cardstuff.draw(clist)
    i2 = orig_deck.index(c2)
    orig_deck.pop(i2)
    c3 = cardstuff.draw(clist)
    i3 = orig_deck.index(c3)

    if i1 == i2 and i2 == i3:
        msg = "***Suspicious output***:"
        msg = msg + " seems like the drawn card is not randomly picked\n"
        msg = msg + "\tbut is always drawn from the same position.\n"
        msg = msg + "Consider testing in Python interactive mode"
        print(msg)
        sys.exit()

    print("Finished running test_draw")


def test_less_than():
    """Test cardstuff.less_than"""
    print("Running test_less_then")

    # We're using a list of lists to compactly encode test cases.
    # Format of sublists: [card1, card2, whether card1 is "less than" card2].
    # We don't guarantee that this is a thorough set of test cases.
    test_cases = [
        [card_labv1.Card(2,10), card_labv1.Card(2,11), True],
        [card_labv1.Card(3,10), card_labv1.Card(2,11), True],
        [card_labv1.Card(2,13), card_labv1.Card(2,11), False],
        [card_labv1.Card(3,10), card_labv1.Card(2,1), False],
        [card_labv1.Card(3,10), card_labv1.Card(3,10), False],
        [card_labv1.Card(3,10), card_labv1.Card(2,10), False],
        [card_labv1.Card(0,10), card_labv1.Card(2,10), True],
        [card_labv1.Card(3,2), card_labv1.Card(2,3), True]
    ]

    for tcase in test_cases:
        card1 = tcase[0]
        card2 = tcase[1]
        answer = tcase[2]
        cornellasserts.assert_equals(answer, cardstuff.less_than(card1, card2))

    print("finished test_less_than")


def test_draw_poker_hand():
    """Some light checking of draw_poker_hand"""
    print("Running test_draw_poker_hand")

    deck = card_labv1.full_deck()
    orig_len = len(deck)
    check_deck = deck[:]  # Copy of deck; not to be modified.

    hand = cardstuff.draw_poker_hand(deck)
    print('Drew the following, which should be a poker hand:', end=' ')
    card_labv1.print_cards_condensed(hand)
    print('The deck now has length ' + str(len(deck)), end=' ')
    print('and contains', end=': ')
    card_labv1.print_cards_condensed(deck)

    # check that hand got exactly five Cards
    assert len(hand) == 5, "hand is not the expected length."
    for c in hand:
        assert isinstance(c, card_labv1.Card), "something is not a Card"

    # check that the Cards in hand are in reversed sorted order.
    for i in range(len(hand)-1):
        assert hand[i] > hand[i+1], "The cards do not seem to be in the right order."

    # check that 5 Cards in hand were removed from the deck
    cornellasserts.assert_equals(orig_len-5, len(deck))
    # check that none of the cards in the hand are in the deck
    for c in hand:
        assert c not in deck, "a Card in the hand wasn't removed from the deck."

    # Check that the order of deck was not otherwise changed.
    # Assert: hand consists of 5 distinct Cards from a normal deck
    # Assert: == for Cards is correctly implemented
    hand_indices = []  # will be indices of hand Cards in check_deck
    for c in hand:
        hand_indices.append(check_deck.index(c))
    expected_deck = []  # will be check_deck minus drawn Cards
    for j in range(len(check_deck)):
        if j not in hand_indices:
            expected_deck.append(check_deck[j])  # Put in Card not in hand

    for i in range(len(expected_deck)):
        cornellasserts.assert_equals(expected_deck[i], deck[i])

    print("Finished test_draw_poker_hand")



if __name__ == '__main__':
    test_draw()
    print()
    test_less_than()
    print()
    test_draw_poker_hand()
    print()
    print('All tests for cardstuff passed.')
    print('You must have played your cards right!')
