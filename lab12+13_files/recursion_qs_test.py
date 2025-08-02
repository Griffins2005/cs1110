"""Test cases for the required lab recursion problems. Omitting specs on the test
procedures because their purpose are clear from the procedure names.

Author: Lillian Lee (LJL2) and Walker White (wmw2)
Version: Mar 16, 2025

"""

import cornellasserts as ca  # Use the name "ca" rather than the longer "cornellasserts"
import recursion_qs

# We need the class Doll from module russian_doll. 
# Because of the lab system's setup, we use this type of import statement
# to avoid needing to say russian_doll.Doll; instead, we write Doll.
from russian_doll import Doll  

import inspect  # For automatically getting function name


def test_even_factorial():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    correct = 2
    result = recursion_qs.even_factorial(2)
    ca.assert_equals(correct, result)

    for n in range(4,26,2):
        correct *= n
        print('\ttrying '+str(n)+", correct would be "+str(correct))
        result = recursion_qs.even_factorial(n)
        ca.assert_equals(correct, result)
    print("All test cases passed for " + fn_name + "\n")

def test_sum_it():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    # Format: each item in the list is a 2-item list, where the first item
    # is a test input and the second is the expected answer
    test_cases = [
        [-2,   -2],  # just an int
        [[3],   3],  # single-element list
        [[],    0],  # empty list
        [[4, -1],     3],  # negative number
        [[4, 4],     8],
        [[4, [10, 11]], 25],  # simple nested list
        [[0, [2, 5, []], 8, [-10, -1]],    4],  # one component is empty list
        [[[2, 5, []], 0,  8, [-10, -1]],   4],  # first item a list
        [[7, [2, 5], [8, [-10, -1]]],     11],
        [[7, 0, [2, 5, []], [8, [-10, -1]]], 11]  #first two items not lists
    ]

    # Create a copy to verify whether any changes happened to lists.
    test_cases_copy = [
        [-2,   -2],  # just an int
        [[3],   3],  # single-element list
        [[],    0],  # empty list
        [[4, -1],     3],  # negative number
        [[4, 4],     8],
        [[4, [10, 11]], 25],  # simple nested list
        [[0, [2, 5, []], 8, [-10, -1]],    4],  # one component is empty list
        [[[2, 5, []], 0,  8, [-10, -1]],   4],  # first item a list
        [[7, [2, 5], [8, [-10, -1]]],     11],
        [[7, 0, [2, 5, []], [8, [-10, -1]]], 11]  #first two items not lists
    ]

    fns_to_test = [recursion_qs.sum_it]
    for fn in fns_to_test:
        print("\tTesting " + fn.__name__)
        for idx in range(len(test_cases)):
            test_input = test_cases[idx][0]
            copy_test_input = test_cases_copy[idx][0]
            correct = test_cases[idx][1]

            print('\ttrying ' + str(test_input))
            ca.assert_equals(correct, fn(test_input))

            # set up test for whether input was changed
            errormsg = "Seems like input list was changed.\n" + \
            "Original input: " + str(copy_test_input) + "\n" + \
            "Input is now: "  + str(test_input) + "\n" 
            assert test_input == copy_test_input, errormsg

    print("All test cases passed for " + fn_name + "\n")

# Helper function.
def _compare_attrs(doll1, doll2):
    """ Return True if the name, innerDoll, and hasSeam attributes
    are the same for the two dolls. Halts with error otherwise.

    doll1 is a Doll
    doll2 is a Doll
    """

    # Employ a precondition check to help students diagnose errors
    for doll in [doll1, doll2]:
        ca.assert_equals(True, isinstance(doll, Doll))
    ca.assert_equals(True, doll1.name == doll2.name)
    ca.assert_equals(True, doll1.innerDoll == doll2.innerDoll)
    ca.assert_equals(True, doll1.hasSeam == doll2.hasSeam)
    return True


def test_num_dolls():
    fn_name = inspect.stack()[0][3]  # Get name of function automatically
    print("Running " + fn_name)

    d1 = Doll("Dmitry", None)
    d2 = Doll("Catherine", d1)
    d3 = Doll("Boris", d2)
    d4 = Doll("Aleksandr", d3)
    dolls = [d1, d2, d3, d4]

    # Copies to check against for changes to dolls
    d1copy = Doll("Dmitry", None)
    d2copy = Doll("Catherine", d1copy)
    d3copy = Doll("Boris", d2copy)
    d4copy = Doll("Aleksandr", d3copy)   
    copies = [d1copy, d2copy, d3copy, d4copy]

    for i in range(len(dolls)):
        print("Running on doll named "+dolls[i].name)
        ca.assert_equals(i+1, recursion_qs.num_dolls(dolls[i])) 

    # Check for changes to input.
    str_orig_input = []  # Printable record of original input
    for dc in copies:
        str_orig_input.append(str(dc))
    str_current_input = []  # Printable record of input state now
    for d in dolls:
        str_current_input.append(str(d))


    ca.assert_equals(len(dolls), len(copies))
    for idx in range(len(dolls)):
        _compare_attrs(dolls[idx], copies[idx])

    print("All test cases passed for " + fn_name + "\n")   


def test_doll_list_names():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    amy=Doll("Amy", None)
    abebe=Doll("Abebe", None)
    wei=Doll("Wei", None)
    walter=Doll("Walter", None)
    walter2=Doll("Walter", None)
    wigbert=Doll("Wigbert", None)
    thor = Doll("Thor", None)

    alist=[amy,abebe]
    wlist=[wei,walter,walter2,wigbert]
    a_and_w =[alist, wlist]
    dolls = [a_and_w, thor]  # nested list
    dolls2 = [a_and_w, thor, []]

    print("\ttesting empty list as input")
    ca.assert_equals([], recursion_qs.doll_list_names([]))

    print("\ttesting single Doll as input")
    ca.assert_equals(["Wigbert"], recursion_qs.doll_list_names(wigbert))

    print("\ttesting non-nested list")
    ca.assert_equals(["Abebe", "Amy"], recursion_qs.doll_list_names(alist))

    print("\ttesting non-nested list with repeat")
    ca.assert_equals(["Walter", "Walter", "Wei", "Wigbert"], 
                     recursion_qs.doll_list_names(wlist))

    print("\tTesting deep list of Dolls")
    ca.assert_equals(["Abebe", "Amy", "Thor", "Walter", "Walter", "Wei", "Wigbert"],
                     recursion_qs.doll_list_names(dolls))
    
    print("\tTesting deep list with an empty list in it")
    ca.assert_equals(["Abebe", "Amy", "Thor", "Walter", "Walter", "Wei", "Wigbert"],
                     recursion_qs.doll_list_names(dolls2))



    # Check that the known attributes of the objects didn't change.
    # (More advanced Python could be used to check that no attributes were added.)
    ca.assert_equals('Amy', amy.name)
    ca.assert_equals(None, amy.innerDoll)
    ca.assert_equals(False, amy.hasSeam)
    ca.assert_equals('Abebe', abebe.name)
    ca.assert_equals(None, abebe.innerDoll)
    ca.assert_equals(False, abebe.hasSeam)
    ca.assert_equals('Wei', wei.name)
    ca.assert_equals(None, wei.innerDoll)
    ca.assert_equals(False, wei.hasSeam)
    ca.assert_equals('Walter', walter.name)
    ca.assert_equals(None, walter.innerDoll)
    ca.assert_equals(False, walter.hasSeam)
    ca.assert_equals('Walter', walter2.name)
    ca.assert_equals(None, walter2.innerDoll)
    ca.assert_equals(False, walter2.hasSeam)
    ca.assert_equals('Wigbert', wigbert.name)
    ca.assert_equals(None, wigbert.innerDoll)
    ca.assert_equals(False, wigbert.hasSeam)
    ca.assert_equals('Thor', thor.name)
    ca.assert_equals(None, thor.innerDoll)
    ca.assert_equals(False, thor.hasSeam)


    print("All test cases passed for " + fn_name + "\n")


# STUDENTS: the next line of code ensures that the indented lines are only
# executed if this script is run at the command line (i.e., they are NOT run
# if this file is imported as a module)
if __name__ == '__main__':

    for testf in [test_even_factorial, test_sum_it, test_num_dolls, test_doll_list_names]:
        testf()  # run each test function

    print("*** All tests passed. Terrific! ***")
