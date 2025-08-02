"""
Functions to convert a word to Pig Latin.

Author(s):
Version:

 Skeleton by Walker White (wmw2), Lillian Lee (LJL2), Feb 2025
"""

# helper for first_vowel; students should not use this directly.
def my_find(letter, s):
    """Returns: position of letter in s, or len(s) if letter not in s.

    Precondition: letter is a lowercase letter
        s is a possibly empty string of lowercase letters."""

    if letter in s:
        return s.index(letter)
    else:
        return len(s)


# helper for students, who should use it without modification
def first_vowel(w):
    """Returns: position of the first vowel in w, or len(w) if there is no vowel.
    Vowels are defined as in the lab instructions.

    Precondition: w is a nonempty string consisting only of lowercase letters."""

    # best_location is smallest index found so far of a vowel;
    # it has value len(w) if none found yet
    best_location = len(w)
    best_location = min(best_location, my_find('a', w))
    best_location = min(best_location, my_find('e', w))
    best_location = min(best_location, my_find('i', w))
    best_location = min(best_location, my_find('o', w))
    best_location = min(best_location, my_find('u', w))

    # can only count a y if w has at least one letter in it
    if len(w) > 1 and 'y' in w[1:]:
        best_y_location = 1 + my_find('y', w[1:])
        best_location = min(best_location, best_y_location)

    return best_location


def pigify(w):
    """Returns: copy of w converted to Pig Latin according to the lab
    instructions.

    Preconditions:
       w is a nonempty string consisting of only lowercase letters.
       If w begins with a 'q', then the next letter is a 'u'.

    """
    # STUDENTS: Use the helper function first_vowel defined above
    vowel_index = first_vowel(w)  # Find the index of the first vowel

    # starts with a vowel
    if vowel_index == 0:
        return w + "hay"

    # starts with "qu"
    elif w.startswith("qu"):
        return w[2:] + "quay"

    # starts with consonant(s)
    else:
        return w[vowel_index:] + w[:vowel_index] + "ay"
 # PLACEHOLDER: REPLACE WITH YOUR IMPLEMENTATION
