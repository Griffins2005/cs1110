"""
Demonstration of sorting algorithms.

Authors: Walker White (wmw2), Michael Clarkson (mrc26)
Version: 5/5/25
"""


def swap(b, i, j):
    """
    Swap b[i] and b[j].

    Precondition: i and j are valid indices in list b.
    """
    temp = b[i]
    b[i] = b[j]
    b[j] = temp


def push_down(b, upper_end):
    """
    Push down b[upper_end] into its proper place to make
    b[0:upper_end+1] sorted.

    Preconditions: upper_end is a valid index in list b,
    and b[0:upper_end] is sorted.
    """

    idx_of_target = upper_end

    # Algorithm: Keep swapping the target with its left neighbor
    # until one of two things happens:
    #   (i) the target reaches the beginning of the list,
    #       ie. idx_of_target == 0; or
    #  (ii) b[idx_of_target-1] < b[idx_of_target].
    # Either way, the target is then in the correct sorted place.
    #
    # Invariant: Only b[idx_of_target] is possibly out of place
    # in b[0:upper_end+1].
    while idx_of_target != 0 and b[idx_of_target-1] > b[idx_of_target]:
        swap(b, idx_of_target-1, idx_of_target)
        idx_of_target = idx_of_target-1


def insertion_sort(b):
    """
    Sort list b in ascending order using insertion sort.
    """
    for i in range(len(b)):
        push_down(b, i)


def merge(b, lo, mid, hi):
    """
    Merge b[lo:mid] and b[mid:hi] and replace b[lo:hi] with the
    resulting sorted segment.

    Precondition: b[lo:mid] and b[mid:hi] are sorted.
    """
    # Copy the left and right segments into their own lists.
    # See note after functions.
    left_seg = b[lo:mid]
    right_seg = b[mid:hi]
    left_idx = 0
    right_idx = 0
    b_idx = lo

    # Algorithm: As long as neither the left nor the right segment is
    # empty, pick the lesser head value of the two segments and move
    # it into the proper index in list b.
    #
    # Invariant: b[lo:b_idx] contains the left_idx smallest values of left_seg
    # and the right_idx smallest values of right_seg, in sorted order.
    while left_idx < len(left_seg) and right_idx < len(right_seg):
        left_head = left_seg[left_idx]
        right_head = right_seg[right_idx]
        if left_head <= right_head:
            b[b_idx] = left_head
            left_idx = left_idx + 1
        else:
            b[b_idx] = right_head
            right_idx = right_idx + 1
        b_idx = b_idx + 1

    # Exactly one of the two following loops will execute its body,
    # because one of the segments has been exhausted when the loop
    # above stop executing.

    # Copy any remaining values from left_seg into b.
    while left_idx < len(left_seg):
        b[b_idx] = left_seg[left_idx]
        left_idx = left_idx + 1
        b_idx = b_idx + 1

    # Copy any remaining values from right_seg into b.
    while right_idx < len(right_seg):
        b[b_idx] = right_seg[right_idx]
        right_idx = right_idx + 1
        b_idx = b_idx + 1

# ADVANCED NOTE: the splice operations above that create left_seg
# and right_seg are wasteful of space. They increase the space
# requirement from linear to linearithmic. A better but more
# complicated implementation would create a single scratch-space list
# in merge() and pass that to all the helper functions to use
# for copying.


def merge_sort_segment(b, lo, hi):
    """
    Sort list segment b[lo:hi] in ascending order using merge sort.
    """
    segment_length = hi - lo
    if segment_length <= 1:
        return

    mid = (lo + hi) // 2
    merge_sort_segment(b, lo, mid)
    merge_sort_segment(b, mid, hi)
    merge(b, lo, mid, hi)


def merge_sort(b):
    """
    Sort list b in ascending order using merge sort.
    """
    merge_sort_segment(b, 0, len(b))


import random


def test_sort(sort_function):
    """
    Compare the result of sort_function() to the built-in sorted() function.
    Do that many times with random lists to see if any discrepancy can be
    detected.
    """
    print(f'Start testing {sort_function.__name__}.')
    N = 10_000 # number of tests
    K = 100 # max list length
    for _ in range(N):
        # Generate a random list length in 1..K
        L = random.randint(1,K)
        # Generate a random list of length L containing elements in 1..L.
        lst = random.choices(range(L), k=L)
        # Create a sorted copy of the list using the built-in sorting function.
        library_sorted_lst = sorted(lst)
        # Sort the list using our own implementation of the sort function.
        sort_function(lst)
        # Compare the results
        assert lst == library_sorted_lst, \
            f'Discrepancy!\n{sort_function.__name__}(): {lst}\nlibrary sorted(): {library_sorted_lst}\n'
    print(f'Done testing {sort_function.__name__}.')


if __name__ == '__main__':
    test_sort(insertion_sort)
    test_sort(merge_sort)