# Lillian Lee (LJL2) and Walker White (wmw2)
# March 2022

"""Test code for loop_practice."""

import loop_practice
import cornellasserts as ca
import inspect  # Used to get function names automatically:
                # inspect.stack()[0] is the "highest" frame on the call stack
import random


def test_lesser_than():
    """Test lesser_than and lesser_than2."""

    # A generic line that can be pasted into any function;
    # retrieves the name of current function from its frame on the stack.
    # Each item in the list returned by inspect.stack() is a call frame.
    # You can print out the frame at the top of the stack by:
    #     print(str(inspect.stack()[0])
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    # We turn to dictionaries and for-loops to make writing test cases less
    # tedious.
    # The keys are tuples representing the two inputs to lesser_than.
    # The values are the expected answers for those two inputs.
    # We have to use tuples because dictionaries don't allow the keys to be
    # "hashable".

    # Format:
    #      (input1, input2): expected_value
    # where input1 is a tuple version of an input list.
    test_cases = {((5, 9, 1, 7), -1): 0,
                  ((5, 9, 1, 7), 1): 0,
                  ((5, 9, 1, 7), 5): 1,  
                  ((5, 9, 1, 7), 6): 2,
                  ((5, 9, 1, 7), 9): 3,
                  ((5, 9, 1, 7), 10): 4,
                  ((), -2): 0,  # testing empty list
                  ((), 2): 0,
                  ((4, 5, 6), 1): 0,
                  ((4, 5, 6), 7): 3,
                  ((4, 4, 4), 7): 3  # testing list with duplicates
                  }

    for test_input in test_cases:
        print("\tTesting input " + str(test_input))
        input_list = list(test_input[0])  # Convert from tuple to list
        orig = input_list[:]  # Create a copy to check that nothing is changed
                              # by the function being tested
        input_value = test_input[1]

        # Test that output is correct
        ca.assert_equals(test_cases[test_input],
                         loop_practice.lesser_than(input_list, input_value))

        # Test that the input list was not changed
        ca.assert_equals(orig, input_list)


def test_perfects():
    """Test perfects."""
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    # Construct questions and their number of perfect subquestions.
    # Have to use tuples inside dictionary keys. Will convert to lists later.
    test_cases = {
        ((0, 2), (3, 4)): 0,
        ((0, 2), (4, 4)): 1,
        ((3, 3), (7, 7), (5, 5)): 3,
        ((1, 1), (6, 7), (5, 5), (2, 2), (0, 2)): 3
    }

    for test_input in test_cases:
        correct = test_cases[test_input]
        print("\tTesting input " + str(test_input))
        ca.assert_equals(correct, loop_practice.perfects(test_input))
        

def test_uniques():
    """Test uniques."""

    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    # Format: each key is a tuple version of an input to function uniques.
    # We can't use lists because dictionaries don't allow them for keys.
    test_cases = {
        (5, 9, 5, 7): 3,  # 5 is duplicated once
        (1, 3, 5, 7): 4,  # All unique
        (5, 1, 3, 5, 3, 5, 5, 5): 3,  # 1, 3, and 5
        (13, "hola", 'b', 7, 'hola', True, False, 2): 7,  # Mixed types
        (5, 5, 1, 'a', 5, 'a'): 3,
        (-1, -1, -1, -1): 1,  # All duplicates
        (): 0,  # empty input
    }

    for test_input in test_cases:
        print("\tTesting input " + str(test_input))

        input_list = list(test_input)
        orig = input_list[:]  # Create a copy to check that nothing is changed
                              # by the function being tested

        # Test that output is correct
        ca.assert_equals(test_cases[test_input], loop_practice.uniques(input_list))

        # Test that the input list was not changed
        ca.assert_equals(orig, input_list)


# STUDENTS: the next line of code ensures that the indented lines are only
# executed if this script is run at the command line (i.e., they are NOT run
# if this file is imported as a module)
if __name__ == '__main__':

    # you can have a list of functions!
    fns_to_run = [test_lesser_than, test_perfects, test_uniques]

    for ind in range(len(fns_to_run)):
        fn = fns_to_run[ind]
        fn()

print("All tests passed. That's terrific!")


