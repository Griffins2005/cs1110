"""

Functions for testing whether a string contains a vowel
and for editing a string.

CAVEATS:

This module exists for students to practice writing test cases and debugging.
Hence, the distributed version may may contain errors.

Authors: Walker M. White (wmw2), Lillian Lee (LJL2)
Version: Feb 2025
"""


def has_a_vowel(s):
    """
    Returns: True if s has at least one vowel (a, e, i, o, or u)

    This function does not count y as a vowel.

    Parameter s: a string to check
    Precondition: s is a non-empty string with all lower case letters
    """
    # The implementation below may have intentional errors in it.
    return 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s


def replace_first(word, target, rep):
    """Returns: a copy of string `word` with the FIRST instance of string
    `target` in `word` replaced by string `rep`.

    Example: replace_first('THanks', 'H', 'h') -> 'Thanks'


    `target` has length >=1 and appears in `word`.
    All the arguments have type str.
    """
    # The implementation below may have intentional errors in it.


    pos = word.index(target)  # where the first target starts
    print("DEBUG: pos is: " + repr(pos))

    before = word[:pos]  # part of word up to but not including first target
    print("DEBUG: before is: " + repr(before))

    after = word[pos+len(target):] # part of word after target
    print("DEBUG: after is: " + repr(after))

    result = before + rep + after  # desired output
    print("DEBUG: result is: " + repr(result))
    return result
