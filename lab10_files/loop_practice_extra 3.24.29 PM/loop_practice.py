# Lillian Lee (LJL2) and Walker White(wmw2)
# Mar 2025
"""For-loop practice functions"""


def lesser_than(thelist, value):
    """Returns: number of items in thelist that are strictly less than `value`.
    Does not change thelist itself.
    Preconditions: thelist is a (possibly empty) list of ints.
                   `value` is an int.

    Example:  lesser_than([5, 9, 1, 7], 9) -> 3
    """
    results = []
    count = 0
    for num in thelist:
        if num < value:
            count = count + 1
    return count
      # STUDENTS: replace with an implementation that makes effective use
          # of a for-loop.







def perfects(exam):
    """Returns: the number of perfect subquestions answered on `exam`.

    A graded exam consists of a non-empty list of questions.
    Each question is a non-empty list of length-two lists of the form
         [got, poss]
    where `got` is the int score that the student received, and `poss` is the
    int max score achievable on that problem, 0 <= got <= poss.
    """
    count = 0
    # Loop over each question (which is itself a list of [got, poss])
    for question in exam:
        if question[0] == question[1]:
            count += 1
    return count
      # Provide an implementation that makes effective use
          # of for-loops.


def uniques(thelist):
    """Returns: The number of unique elements in thelist.
    Does not modify thelist.

    Examples: unique([5, 9, 5, 7]) -> 3
              unique([5, 5, 1, 'a', 5, 'a']) -> 3

    Precondition: thelist is a (possibly empty) list."""
    # You *must* implement this with a for-loop.
    # You are *not* allowed to use counts() to see if an item occurs more
    # than once.
    #
    # Hint1: You need to keep track of all the items you've already seen.
    #        One strategy is to start with a new empty list called new_items,
    #        and gradually append to new_items any previously unseen item.
    #
    #        An alternate strategy is to look to see if the current item
    #        existed in any of the prior part of thelist.
    #
    # Hint2: You can check whether `item` is in new_items via
    #           item in new_items  # This is a boolean expression
    #        Similarly, you can do
    #           item not in new_items
    #        or
    #           not item in new_items

    results = []
    count = 0
    if not thelist:
        return 0
    for elem in thelist:
        if elem not in results:
            count = count + 1
            results.append(elem)
    return count

      # STUDENTS:
          # replace with your code, which must make effective use of
          # of a for-loop
