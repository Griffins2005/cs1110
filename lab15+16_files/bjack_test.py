"""
Testing code for bjack.Blackjack

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Version: Mar 25, 2025
"""
import cornellasserts
import card_v2 as card
import bjack


def test_game_init():
    """
    Tests the __init__ method for Blackjack objects
    """
    print('Testing  __init__')
    c1 = card.Card(0, 12)
    c2 = card.Card(1, 10)
    c3 = card.Card(2, 9)
    c4 = card.Card(0, 1)

    # Initialize deck and start game.
    deck = [c1, c2, c3, c4]
    game = bjack.Blackjack(deck)

    cornellasserts.assert_equals([c1, c2], game.playerHand)
    cornellasserts.assert_equals([c3], game.dealerHand)
    cornellasserts.assert_equals([c4], game.deck)
    cornellasserts.assert_equals([c4], deck)  # check that cards were removed

    deck = card.full_deck()  # non-shuffled deck
    game = bjack.Blackjack(deck)
    c1 = card.Card(0, 1)
    c2 = card.Card(0, 2)
    c3 = card.Card(0, 3)
    c4 = card.Card(0, 4)

    cornellasserts.assert_equals([c1, c2], game.playerHand)
    cornellasserts.assert_equals([c3], game.dealerHand)

    # check that right cards were removed
    cornellasserts.assert_equals(card.full_deck()[3:], deck)


def test_game_str():
    """
    Tests the __str__ function for Blackjack objects
    """
    print('Testing method __str__')
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)
    cornellasserts.assert_equals('player: 20; dealer: 9', str(game))

    game.playerHand=[]
    cornellasserts.assert_equals('player: 0; dealer: 9', str(game))
    game.dealerHand.append(card.Card(2,1))
    cornellasserts.assert_equals('player: 0; dealer: 20', str(game))
    game.dealerHand.append(card.Card(2,5))
    cornellasserts.assert_equals('player: 0; dealer: 25', str(game))


def test_game_score():
    """
    Tests the _score method (which is hidden, but we access anyway)
    """
    print('Testing the blackjack _score method')
    # need a dummy game object to call its _score function (and test it)
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    cornellasserts.assert_equals(13, game._score([card.Card(2, 2), card.Card(3, 1)]))
    cornellasserts.assert_equals(13, game._score([card.Card(1, 13), card.Card(0, 3)]))
    cornellasserts.assert_equals(22, game._score([card.Card(1, 1), card.Card(0, 1)]))
    cornellasserts.assert_equals(9, game._score([card.Card(1, 2), card.Card(0, 3), card.Card(3, 4)]))
    cornellasserts.assert_equals(0, game._score([]))


def test_dealerScore():
    """
    Tests the dealerScore method for Blackjack objects
    """
    print('Testing method dealerScore')
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    cornellasserts.assert_equals(9, game.dealerScore())
    game.dealerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.playerHand = [card.Card(1, 13), card.Card(0, 3)]
    cornellasserts.assert_equals(13, game.dealerScore())


def test_playerScore():
    """
    Tests the playerScore method for Blackjack objects
    """
    print('Testing method playerScore')
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    cornellasserts.assert_equals(20, game.playerScore())
    game.playerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.dealerHand = [card.Card(1, 13), card.Card(0, 3)]
    cornellasserts.assert_equals(13, game.playerScore())


def test_playerBust():
    """
    Tests the playerBust method for Blackjack objects
    """
    print('Testing method playerBust')
    # get dummy deck
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    cornellasserts.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10)]
    cornellasserts.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 2), card.Card(1, 9), card.Card(3, 10)]
    cornellasserts.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    cornellasserts.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    cornellasserts.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    cornellasserts.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    cornellasserts.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 2)]
    cornellasserts.assert_true(game.playerBust())

def test_dealerBust():
    """
    Tests the dealerBust method for Blackjack objects
    """
    print('Testing method dealerBust')
    # get dummy deck
    deck = [card.Card(0, 12),  card.Card(2, 9), card.Card(1, 10),]
    game = bjack.Blackjack(deck)

    cornellasserts.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10)]
    cornellasserts.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 2), card.Card(1, 9), card.Card(3, 10)]
    cornellasserts.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    cornellasserts.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    cornellasserts.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    cornellasserts.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    cornellasserts.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    cornellasserts.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 2)]
    cornellasserts.assert_true(game.dealerBust())


# Script code
if __name__ == '__main__':
    test_game_init()
    test_game_score()
    test_dealerScore()
    test_playerScore()
    test_dealerBust()
    test_playerBust()
    test_game_str()

    print('The module bjack passed all tests.')
