"""
A module for a very simple approximation of the game Blackjack

This module provides the class for the Blackjack game, but NOT the cards.
Those are provided in the card module.

Griffins Lelgut (gkl39)
Apr 2,2025
Author: Lillian Lee (LJL2) and Walker White (WMW2)
Version: Mar 25, 2025


"""
import card_v2 as card
import random


class Blackjack:
    """An instance is a game of Blackjack between a single player and a dealer.

    Instance Attributes:
        playerHand [list of Cards, may be empty]: the player's cards
        dealerHand [list of Cards, may be empty]: the dealer's cards
        deck [list of Cards]: list of the remaining Cards to draw from.
            The deck is assumed to hold enough Cards that it won't run out.
    """

    def __init__(self, deck):
        """
        Initializes a new blackjack game with the two hands initialized
        and the game's internal deck set to the remaining cards in `deck`.

        The player's hand playerHand will be the first two cards in `deck`.
        The dealer's hand dealerHand will be the third card in `deck`.
        These three cards are removed from `deck`.

        `deck` is a parameter because we allow the caller, such as a casino,
        to "stack the deck" (choose the arrangement of the cards, insert
        extra cards, etc.) to its advantage!

        Parameter deck: a list of at least three Cards (and nothing other
        than Cards). More than 3 cards is preferable.
        """
        # The player's hand consists of the first two cards from the deck
        self.playerHand = [deck.pop(0), deck.pop(0)]

        # The dealer's hand consists of the next card from the deck
        self.dealerHand = [deck.pop(0)]

        # The remaining cards become the new deck for the game
        self.deck = deck

    def __str__(self):
        """
        Returns the string (replacing the values in angle brackets appropriately)
        player: <player's score>, dealer: <dealer's score>

        Here, we are assuming that all that matters is the score
        (which is True if aces are always 11).

        Example output:
            'player: 12; dealer: 20'
        """
        return 'player: ' + str(self.playerScore()) + '; dealer: ' + str(self.dealerScore())

    def dealerScore(self):
        """
        Returns the score for the dealer.
        """
        return self._score(self.dealerHand)

    def playerScore(self):
        """
        Returns the score for the player.
        """
        return self._score(self.playerHand)

    def playerBust(self):

        """
        Returns True if player has gone bust (score over 21); False otherwise
        """
        return self.playerScore() > 21

    def dealerBust(self):
        """
        Returns True if dealer has gone bust (score over 21); False otherwise
        """
        return self.dealerScore() > 21

    # DO NOT MODIFY BELOW THIS LINE
    def play(self):
        """
        Runs a single hand of blackjack.

        This function provides a text-based interface for blackjack.
        It will continue to run until the end of the game, or there
        are no cards left.
        """

        self._print_initial_info()

        # While player has not bust, ask if player wants to draw
        player_halted = False  # True player wants to halt, False otherwise
        while not self.playerBust() and not player_halted:
            # ri: input received from player
            ri = self._prompt_player('Type h for new card, s to stop: ',['h', 's'])

            player_halted = (ri == 's')
            if (not player_halted) and self.deck:
                drawn = self.deck.pop(0)
                self.playerHand.append(drawn)
                print('You drew the ' + str(drawn))
                print()
            elif (not player_halted) and not self.deck:
                print('There are no cards left to draw')
                print()
                player_halted = False

        if self.playerBust():
            print('You went bust, dealer wins.')
        else:
            self._dealer_turn()

        print()
        print('The final scores were ' + str(self))

    # HELPER METHODS
    def _score(self, hand):
        """
        Returns a simplified-blackjack score for a given hand

        This is a helper method for computing the score of a given hand.  In our
        version of blackjack, aces always count as 11 points.  Face cards count
        as 10 points and Suits do not matter.

        Example: input: [2 of Hearts, Ace of spades], output: 13
        Example: input: [King of Diamonds, 3 of Clubs], output 13

        Parameter hand: The blackjack hand
        Precondition: hand is a list of Cards"""
        s = 0  # score to return
        for c in hand:
            if c._rank >= 11:  # c is a face card
                s = s + 10
            elif c._rank == 1:  # c is an ace
                s = s + 11
            else:
                s = s + c._rank
        return s

    def _print_initial_info(self):
        # Tell player the scoring rules
        print('Welcome to CS 1110 Blackjack.')
        print('Rules: Face cards are 10 points. Aces are 11 points.')
        print('       All other cards are at face value.')
        print()

        # Show initial deal
        print('Your hand: ')
        self._print_cards(self.playerHand)
        print()
        print("Dealer's hand: ")
        self._print_cards(self.dealerHand)
        print()

    def _print_cards(self,clist):
        """
        Prints the cards in list clist.

        Parameter clist: the card list
        Precondition:  clist is a list of Cards, possibly empty.
        """
        for c in clist:
            print(str(c))

    def _prompt_player(self,prompt,valid):
        """
        Returns: the choice of a player from a given prompt.

        This is a helper method for play().  It asks the user a question, and
        waits for a response.  It checks if the response is valid against a
        list of acceptable answers.  If it is not valid, it asks the question
        again. Otherwise, it returns the player's answer.

        Parameter prompt: The question prompt to display to the player
        Precondition: prompt is a string

        Parameter valid: The valid reponses
        Precondition: valid is a list of strings
        """
        # Ask the question for the first time.
        # ri: input received from player
        ri = input(prompt)

        # Continue to ask while the response is not valid.
        while not (ri in valid):
            print('Invalid response.  Answer must be one of '+str(valid))
            print()
            ri = input(prompt)

        return ri

    def _dealer_turn(self):
        """
        Performs the dealer's turn, printing out the result.

        The function uses standard BlackJack rules: the dealer stands above 17,
        but hits otherwise. If the dealer cannot draw a card, the turn is over.
        """
        # Dealer draws until at 17 or above or goes bust
        dealer_halted = (self.dealerScore() >= 17)
        while not self.dealerBust() and not dealer_halted:
            if self.deck:
                drawn = self.deck.pop(0)
                self.dealerHand.append(drawn)
                dealer_halted = (self.dealerScore() >= 17)
                print('Dealer drew the ' + str(drawn))
            else:
                print('Dealer ran out of cards')
                dealer_halted = True

        print()
        if (self.dealerBust()):
            print('Dealer went bust, you win!')
        elif (self.dealerScore() > self.playerScore()):
            print('Dealer outscored you, dealer wins.')
        elif (self.dealerScore() < self.playerScore()):
            print('You outscored dealer, you win!')
        else:
            print('The game was a tie.')


# Script code
if __name__ == '__main__':
    # Create a new shuffled full deck
    deck = card.full_deck()
    random.shuffle(deck)

    # Start a new game. Player gets two cards; dealer gets one
    game = Blackjack(deck)
    game.play()
