"""
Quick check of behavior
"""
from onioncard import OnionCard, full_deck
from card_v2 import list_str

def small_test():
    """Some tests suggested in the handout."""

    print("Trying out initializer by creating an OnionCard (the 10 of Cups)")
    print(OnionCard(6, 10))

    print("Trying out the str methods for two OnionCards.")
    print("One is 'normal' (4 of Diamonds); the other is the Ace of Cups.")
    regular = OnionCard(1,4)
    unusual = OnionCard(6,1)
    print(str(regular) + ", " + str(unusual))

    print("Testing full_deck()")
    print(list_str(full_deck()))


if __name__ == '__main__':
    small_test()
