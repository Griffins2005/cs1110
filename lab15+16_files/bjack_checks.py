"""

   Some light checking for module blackjack.

   If you want this testing file to have less output, run it on the command
   line with the argument 'quiet', like this:
        python blackjack_checks.py quiet

Author: L. Lee (LJL2), S. Marschner (SRM2), and W. White (WMW2)
Version: Mar 25, 2025
"""

import cornellasserts as ca 
import bjack
import card_v2 as cv2  
import sys
import inspect  # Used to get function names automatically:
                # inspect.stack()[0] is the "highest" frame on the call stack


# Possible card lists and their scores.
test_cases_in_common = [
    # Elements are pairs.
    # In a pair, the 1st item is a list of cards, the second the correct score.
    [[cv2.Card(code='AD')], 11],  # A single ace
    [[cv2.Card(code='2H'), cv2.Card(code='5S')], 7 ],   # No face cards
    [[cv2.Card(code='2C'), cv2.Card(code='AH')], 13],   # Includes an ace
    [[cv2.Card(code='KD'), cv2.Card(code='2D')], 12],   # Includes a king
    [[cv2.Card(code='QH'), cv2.Card(code='7D')], 17],   # Includes a queen
    [[cv2.Card(code='JS'), cv2.Card(code='8C')], 18],   # Includes a jack
    [[cv2.Card(code='TH'), cv2.Card(code='AC')], 21],   # a ten and an ace
    [[cv2.Card(code='AD'), cv2.Card(code='AH')], 22],   # Two aces
    [[cv2.Card(code='2C'), cv2.Card(code='3C'), cv2.Card(code='4S')], 9],
    [[cv2.Card(code='2C'),
      cv2.Card(code='2D'),
      cv2.Card(code='2H'),
      cv2.Card(code='2S'),
      cv2.Card(code='3C')], 11],
    [[cv2.Card(code='5H'), cv2.Card(code='AS')], 16],
    [[cv2.Card(code='KD'), cv2.Card(code='3C')], 13],
    [[], 0] # empty list
    ]

# Possible hands and whether they are bust are not.
# Remember that in our rules, Aces count as 11.
test_cases_bust=[
    # Elements are pairs
    # In a pair, the 1st item is a list of cards, the 2nd the correct "bust" value
    [[cv2.Card(code='AD'), cv2.Card(code="TC")], False],
    [[cv2.Card(code='AC'), cv2.Card(code='TD'), cv2.Card(code='2C')], True],
    [[cv2.Card(code='TS'), cv2.Card(code='TD'), cv2.Card(code='AC')], True],
    [[cv2.Card(code='JC'), cv2.Card(code='TS'), cv2.Card(code='AC')], True],
    [[cv2.Card(code='QH'),
     cv2.Card(code='TD'),
     cv2.Card(code='AS'),
     cv2.Card(code='AC')], True],
    [[cv2.Card(code='AD'),], False],
    [[cv2.Card(code='2H'), cv2.Card(code='5S')], False],
    [[cv2.Card(code='2C'), cv2.Card(code='AH')], False],
    [[cv2.Card(code='KD'), cv2.Card(code='2D')], False],
    [[cv2.Card(code='QH'), cv2.Card(code='7D')], False],
    [[cv2.Card(code='JS'), cv2.Card(code='8C')], False],
    [[cv2.Card(code='TH'), cv2.Card(code='AC')], False],
    [[cv2.Card(code='AD'), cv2.Card(code='AH')], True],
    [[cv2.Card(code='2C'), cv2.Card(code='3C'), cv2.Card(code='4S')], False],
    [[cv2.Card(code='2C'),
     cv2.Card(code='2D'),
     cv2.Card(code='2H'),
     cv2.Card(code='2S'),
     cv2.Card(code='3C')], False],
    [[cv2.Card(code='5H'), cv2.Card(code='AS')], False],
    [[cv2.Card(code='KD'), cv2.Card(code='3C')], False],
    [[], False]
    ]

# It's useful to have a dummy game around, where the actual player and dealer
# hands will later be overwritten in testing
def make_dummy_game():
    """Returns a dummy blackjack game."""
    clist = [cv2.Card(code='QC'), cv2.Card(code='TD'), cv2.Card(code='9H')] 
    return bjack.Blackjack(clist)



def test_init(verbose):
    """Test initializer of blackjack objects.
    Extra info printed if `verbose` is True. """

    print_testing('start')

    # Small test
    c1 = cv2.Card(0, 12)
    c2 = cv2.Card(1, 10)
    c3 = cv2.Card(2, 9)
    c4 = cv2.Card(0, 1)
    start_deck = [c1, c2, c3, c4]
    if verbose:
        print("testing start deck of " + cv2.list_str(start_deck))

    game = bjack.Blackjack(start_deck)
    ca.assert_equals(set([c1, c2]), set(game.playerHand))  # Sets ignore order,
                                                           # which is handy
    ca.assert_equals([c3], game.dealerHand)
    ca.assert_equals([c4], start_deck)  # Check that cards were removed
    assert start_deck is game.deck, (# Check that game deck is the start_deck
                                     # object.
        ("The Blackjack game's `deck` is the wrong object. Maybe you created " +
         "a new object for the deck by accident?"))

    # Bigger test.
    start_deck = cv2.full_deck()
    if verbose:
        print("testing start deck of " + cv2.list_str(start_deck))
    game = bjack.Blackjack(start_deck)
    ca.assert_equals(set([cv2.Card(0, 1), cv2.Card(0, 2)]), set(game.playerHand))
    ca.assert_equals([cv2.Card(0, 3)], game.dealerHand)
    # Check card removal
    ca.assert_equals(cv2.full_deck()[3:], start_deck)
    assert start_deck is game.deck, (   # Check that game deck is the start_deck
                                        # object.
        ("The Blackjack game's `deck` is the wrong object. Maybe you created " +
         "a new object for the deck by accident?"))

    print_testing('end')

def test_str(verbose):
    """Test __str__ function for Blackjack objects.
    Extra info printed if `verbose` is True."""

    print_testing('start')

    # Test cases:
    test_cases = [
        # Items are pairs
        # each pair: first a list of playerhand and dealerhand. 
        # then the desired output of __str__
        [[[cv2.Card(code='KH'), cv2.Card(code='TD')], # playerhand
          [cv2.Card(code='9H')] # dealerhand
          ],
         'player: 20; dealer: 9'],
        [[[], # empty playerhand
          [cv2.Card(code='3H')]], # dealerhand
         'player: 0; dealer: 3'],
        [[[cv2.Card(code='7H'), cv2.Card(code="AH")], 
          []], # empty dealerhand
         'player: 18; dealer: 0'],
        [[[cv2.Card(code='9H'), cv2.Card(code="4H")],
          [cv2.Card(code='3S'), cv2.Card(code='KH'), cv2.Card(code='9C')]],
        'player: 13; dealer: 22']
    ]

    game = make_dummy_game()
    for tc in test_cases:
        phand = tc[0][0]
        dhand = tc[0][1]
        if verbose:
            print('\tTesting ' +
                  cv2.list_str(phand) + ' and ' + cv2.list_str(dhand))
        answer = tc[1]
        game.playerHand = phand
        game.dealerHand = dhand
        output = str(game)
        ca.assert_equals(answer, output)

    print_testing('end')

def test_score(verbose):
    """Test _score function.
    Extra info printed if `verbose` is True."""

    print_testing('start')
    game = make_dummy_game()

    for tc in test_cases_in_common:
        testinput = tc[0]
        if verbose:
            print('\tTesting ' + cv2.list_str(testinput))
        answer = tc[1]
        output = game._score(testinput)
        ca.assert_equals(answer, output)

    print_testing('end')

def test_dealerScore(verbose):
    """Test dealerScore function.
    Extra info printed if `verbose` is True."""

    print_testing('start')

    game = make_dummy_game()
    for tc in test_cases_in_common:
        testinput = tc[0]
        if verbose:
            print('\tTesting ' + cv2.list_str(testinput))
        answer = tc[1]
        game.dealerHand = testinput  # Set the dealerHand to be a test case.
        output = game.dealerScore()
        ca.assert_equals(answer, output)

    print_testing('end')


def test_playerScore(verbose):
    """Test playerScore function.
    Extra info printed if `verbose` is True."""

    print_testing('start')

    game = make_dummy_game()
    for tc in test_cases_in_common:
        testinput = tc[0]
        if verbose:
            print('\tTesting ' + cv2.list_str(testinput))
        answer = tc[1]
        game.playerHand = testinput  # Set the playerHand to be a test case.
        output = game.playerScore()
        ca.assert_equals(answer, output)

    print_testing('end')


def test_dealerBust(verbose):
    """Test dealerBust function.
    Extra info printed if `verbose` is True."""

    print_testing('start')

    game = make_dummy_game()
    for tc in test_cases_bust:
        testinput = tc[0]
        if verbose:
            print('\tTesting ' + cv2.list_str(testinput))
        answer = tc[1]
        game.dealerHand = testinput
        output = game.dealerBust()
        ca.assert_equals(answer, output)

    print_testing('end')


def test_playerBust(verbose):
    """Test playerBust function.
    Extra info printed if `verbose` is True."""

    print_testing('start')

    game = make_dummy_game()
    for tc in test_cases_bust:
        testinput = tc[0]
        if verbose:
            print('\tTesting ' + cv2.list_str(testinput))
        answer = tc[1]
        game.playerHand = testinput
        output = game.playerBust()
        ca.assert_equals(answer, output)

    print_testing('end')


# helper
def print_testing(start_or_end):
    """If start_or_end is 'start',
        print message about starting function that called this function
       If start_or_end is 'end'
        print message about ending function that called this function

    Precondition: start_or_end is either 'start' or 'end'"""
    caller = inspect.currentframe().f_back.f_code.co_name
    if start_or_end == 'start':
        print("Starting " + caller)
    elif start_or_end == 'end':
        print(caller + " seems to have passed (didn't crash/stop in the middle).")
        print("\n")   



# Script code
if __name__ == '__main__':

    verbose = True  # Default mode is to give lots of output.
                    # False means give less output

    # Handling arguments from the command line
    if len(sys.argv) > 1:
        # Was called with at least one argument
        if len(sys.argv) == 2 and sys.argv[1] in ["quiet"]:
            # called by "python <this file's name> quiet"
            verbose = False
        else:
            print("Invalid argument(s), only possible argument is 'quiet'.")
            sys.exit()

    fns_to_run = [test_init,
                  test_score, # This function should already be correct,
                              # since we wrote it for you.
                  test_dealerScore,
                  test_playerScore,
                  test_dealerBust,
                  test_playerBust,
                  test_str]


    for ind in range(len(fns_to_run)):
        test_fn = fns_to_run[ind]
        test_fn(verbose)

    print("All checks for blackjack passed.  You win!")
