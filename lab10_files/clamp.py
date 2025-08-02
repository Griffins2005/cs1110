# clamp.py
# YOUR NAME AND NETID HERE;
# PUT THE DATE HERE
# Skeleton of Mar 12, 2022 by L. Lee and W. White.

def clamp(alist, floor, ceiling):
    """
    Does not return anything.  Rather, modifies `alist` so that every element is
    between `floor` and `ceiling`, as follows:

        * Any element less than `floor` is replaced with `floor`.
        * Any element greater than `ceiling` is replaced with `ceiling`.
        * No other elements are changed.

    Example: if `alist` is [-1, 1, 3, 5], then clamp(alist,0,4) changes
    `alist` to have [0,1,3,4] as its contents.

    Preconditions:
        `alist` is a (possibly empty) list of ints
        `floor` and `ceiling are floats or ints, and `floor` <= `ceiling`
    """
    for i in range(len(alist)):
        if alist[i] < floor:
            alist[i] = floor
        elif alist[i] > ceiling:
            alist[i] = ceiling
    # STUDENTS: Implement, making effective use of for-loops.


def outliers(alist, floor, ceiling):
    """Like clamp(), but instead of changing alist,
    returns a new list of indices of elements that are above `ceiling` or
    below `floor`.

    Example: if `alist` is [-1, 1, 3, 5],
      outliers(alist, 0, 4) --> [0, 3].

    Preconditions: as for clamp()."""
    return [i for i in range(len(alist)) if alist[i] < floor or alist[i] > ceiling]
 # STUDENTS: implement, making effective use of for-loops.
