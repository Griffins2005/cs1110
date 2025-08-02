"""
Tests for nested lists functions

Author: Walker M. White (wmw2), w/ extremely minor edits by Lillian Lee (LJL2)
Version:   October 20, 2021  w/ extremely minor edits and added test case Mar 11, 2025 
"""
import cornellasserts
import nested_lists
import copy


def test_row_sums():
    """
    Test procedure for function row_sums

    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function row_sums')
    result = nested_lists.row_sums([[0.8, 0.2], [0.6, 0.9], [0.4, 0.3]])
    cornellasserts.assert_float_lists_equal([1.0, 1.5, 0.7],result)
    result = nested_lists.row_sums([[0.2, -0.6, 0.1], [0.9, 0.8, -1.0]])
    cornellasserts.assert_float_lists_equal([-0.3, 0.7],result)
    result = nested_lists.row_sums([[0.4, 0.8, 0.5, 0.4]])
    cornellasserts.assert_float_lists_equal([2.1],result)
    result = nested_lists.row_sums([[0.3], [0.5], [0.8], [0.4]])
    cornellasserts.assert_float_lists_equal([0.3, 0.5, 0.8, 0.4],result)


def test_place_sums():
    """
    Test procedure for function place_sums

    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function place_sums')

    table = [['I1','I2'], [0.8, 0.2], [0.6, 0.9], [0.4, 0.3]]
    goal  = [['I1','I2','Sum'], [0.8, 0.2, 1.0], [0.6, 0.9, 1.5], [0.4, 0.3, 0.7]]
    temp = nested_lists.place_sums(table)
    # Check that nothing is returned
    cornellasserts.assert_equals(None, temp)
    cornellasserts.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        cornellasserts.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1','I2','I3'], [0.2, -0.6, 0.1], [0.9, 0.8, -1.0]]
    goal  = [['I1','I2','I3','Sum'], [0.2, -0.6, 0.1, -0.3], [0.9, 0.8, -1.0, 0.7]]
    nested_lists.place_sums(table)
    cornellasserts.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        cornellasserts.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1','I2','I3','I4'], [0.4, 0.8, 0.5, 0.4]]
    goal  = [['I1','I2','I3','I4','Sum'], [0.4, 0.8, 0.5, 0.4, 2.1]]
    nested_lists.place_sums(table)
    cornellasserts.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        cornellasserts.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1'], [0.3], [0.5], [0.8], [0.4]]
    goal  = [['I1','Sum'], [0.3, 0.3], [0.5, 0.5], [0.8, 0.8], [0.4, 0.4]]
    nested_lists.place_sums(table)
    cornellasserts.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        cornellasserts.assert_float_lists_equal(goal[pos],table[pos])


### OPTIONAL EXERCISES ###


def test_crossout():
    """
    Test procedure for function crossout.

    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function crossout')

    table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = nested_lists.crossout(table,1,2)
    cornellasserts.assert_float_lists_equal([[0.1,0.3],[1.5,2.3]],result)
    cornellasserts.assert_float_lists_equal(orig,table)

    result = nested_lists.crossout(table,0,0)
    cornellasserts.assert_float_lists_equal([[0.2,0.7],[2.3,0.4]],result)
    cornellasserts.assert_float_lists_equal(orig,table)

    result = nested_lists.crossout(table,2,1)
    cornellasserts.assert_float_lists_equal([[0.1,0.5],[0.6,0.7]],result)
    cornellasserts.assert_float_lists_equal(orig,table)

    table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4],[0.1,0.2,0.3]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = nested_lists.crossout(table,1,2)
    cornellasserts.assert_float_lists_equal([[0.1,0.3],[1.5,2.3],[0.1,0.2]],result)
    cornellasserts.assert_float_lists_equal(orig,table)

    table = [[0.1,0.3,0.5,1.0],[0.6,0.2,0.7,2.0],[1.5,2.3,0.4,3.0]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = nested_lists.crossout(table,1,2)
    cornellasserts.assert_float_lists_equal([[0.1,0.3,1.0],[1.5,2.3,3.0]],result)
    cornellasserts.assert_float_lists_equal(orig,table)

    table = [[1,2],[3,4]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = nested_lists.crossout(table,1,0)
    cornellasserts.assert_float_lists_equal([[2]],result)
    cornellasserts.assert_float_lists_equal(orig,table)

    result = nested_lists.crossout(table,0,1)
    cornellasserts.assert_float_lists_equal([[3]],result)
    cornellasserts.assert_float_lists_equal(orig,table)

    table = [[5]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = nested_lists.crossout(table,0,0)
    cornellasserts.assert_equals([],result)
    cornellasserts.assert_float_lists_equal(orig,table)


# Script code
if __name__ == '__main__':
    test_row_sums()
    test_place_sums()
    test_crossout()

    print('The functions passed all tests')
