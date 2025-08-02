"""Test cases for the optional lab recursion problems.

Go to the bottom of this file and uncomment the test functions you wish to run!

Author: Lillian Lee (LJL2) and Walker White (wmw2)
Version: Mar 16, 2025
"""

import recursion_optional
import cornellasserts as ca

import inspect  # For automatically getting function name

import sys  # For testing printouts
import io  # For testing printouts


def test_print_nested_list():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    test_cases = [
        ["cs1110", "cs1110\n"],
        [['this', ['is', 'a'], 'list', ['list', 'list']],
         "this\nis\na\nlist\nlist\nlist\n"],
        [[[['cs1110', 'opython'], 'nested'], 'recursion', 'test'],
         "cs1110\nopython\nnested\nrecursion\ntest\n"],
        [[['this'], ['is', ['a', ['very', 'very', 'very'], ['nes ted', 'list']]]],
         "this\nis\na\nvery\nvery\nvery\nnes ted\nlist\n"]
    ]
    test_cases_copy = [
        ["cs1110", "cs1110\n"],
        [['this', ['is', 'a'], 'list', ['list', 'list']],
         "this\nis\na\nlist\nlist\nlist\n"],
        [[[['cs1110', 'opython'], 'nested'], 'recursion', 'test'],
         "cs1110\nopython\nnested\nrecursion\ntest\n"],
        [[['this'], ['is', ['a', ['very', 'very', 'very'], ['nes ted', 'list']]]],
         "this\nis\na\nvery\nvery\nvery\nnes ted\nlist\n"]
    ]

    fns_to_test = [recursion_optional.print_nested_list]
    for fn in fns_to_test:
        print("\tTesting " + fn.__name__)
        for idx in range(len(test_cases)):
            tc = test_cases[idx]
            inlist = tc[0]
            copyinlist = test_cases_copy[idx][0]
            answer = tc[1]
            print('\ttrying ' + str(inlist))

            # Magic to be able to store print output somewhere
            old_stdout = sys.stdout
            capturer = io.StringIO()
            sys.stdout = capturer
            recursion_optional.print_nested_list(inlist)
            sys.stdout = old_stdout
            output = capturer.getvalue()
            try:
                ca.assert_equals(answer, output)
            except:
                print()
                print('What SHOULD have been printed:')
                print(answer)
                print()
                print("The code's output")
                print(output)
                exit()

            # check for changes to input
            errormsg = "Seems like input list was changed.\n" + \
                   "Original input: " + str(copyinlist) + "\n" + \
                   "Input is now: "  + str(tc[0]) + "\n"
            assert inlist == copyinlist, errormsg

    print("All test cases passed for " + fn_name + "\n")


def test_embed():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)
    ca.assert_equals(0, recursion_optional.embed('cs1110'))
    ca.assert_equals(1, recursion_optional.embed(['cs1110']))
    ca.assert_equals(1, recursion_optional.embed(['cs1110', 'opython', 'typoon']))
    ca.assert_equals(3,
                     recursion_optional.embed(['cs1110',
                                           ['opython', ['recursion'], 'typoon']]))
    print("All test cases passed for " + fn_name + "\n")


def test_max_nested_list():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)
    ca.assert_equals(0, recursion_optional.max_nested_list(0))
    ca.assert_equals(8, recursion_optional.max_nested_list([0, [2, 5], 8, [-10, -1]]))
    ca.assert_equals(1, recursion_optional.max_nested_list([[[[1]]]]))
    ca.assert_equals(1110,
                     recursion_optional.max_nested_list([[[[1, 1110],2],3],4]))
    print("All test cases passed for " + fn_name + "\n")

def test_flatten_nested_list():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)
    fns_to_test = [recursion_optional.flatten_nested_list]
    for flatten_fn in fns_to_test:
        print("\ttesting " + flatten_fn.__name__)
        ca.assert_equals(['cs1110'],
                         flatten_fn(['cs1110']))
        ca.assert_equals(['this', 'is', 'a', 'list', 'list', 'list'],
                         flatten_fn(['this',
                                    ['is', 'a'],
                                    'list',
                                    ['list', 'list']]))
        ca.assert_equals(['cs1110', 'opython', 'nested', 'recursion', 'test'],
                         flatten_fn([[['cs1110', 'opython'], 'nested'], 'recursion', 'test']))

        mylist = ['cs1110']
        ca.assert_equals(False,
                         mylist is flatten_fn(mylist))

    print("All test cases passed for " + fn_name + "\n")


#################################################


def test_reverse1():

    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)
    reverse_fn = recursion_optional.reverse1

    inputlist = []
    ca.assert_equals([], reverse_fn(inputlist))

    inputlist = [3]
    ca.assert_equals([3], reverse_fn(inputlist))

    inputlist = [3, 2, 1]
    ca.assert_equals([1, 2, 3], reverse_fn(inputlist))

    inputlist = [4, 4, 3, 17, 4, 9]
    ca.assert_equals([9, 4, 17, 3, 4, 4], reverse_fn(inputlist))

    # check for returning a copy
    print("checking whether on [3] a copy of [3] is returned")
    mylist = [3]
    ca.assert_equals(False, mylist is reverse_fn(mylist))

    print("All test cases passed for " + fn_name + "\n")


def test_reverse2():

    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    reverse_fn = recursion_optional.reverse2

    inputlist = []
    ca.assert_equals([], reverse_fn(inputlist))

    inputlist = [3]
    ca.assert_equals([3], reverse_fn(inputlist))

    inputlist = [3, 2, 1]
    ca.assert_equals([1, 2, 3], reverse_fn(inputlist))

    inputlist = [4, 4, 3, 17, 4, 9]
    ca.assert_equals([9, 4, 17, 3, 4, 4], reverse_fn(inputlist))

    # check for returning a copy
    print("checking whether on [3] a copy of [3] is returned")
    mylist = [3]
    ca.assert_equals(False, mylist is reverse_fn(mylist))

    print("All test cases passed for " + fn_name + "\n")



#################################################


def test_replace():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    # format: each item is a four-item list:
    # the list of numbers
    # the target
    # the replacement
    # what the resulting list should look like
    test_cases = [
        [[5, 6], 5, 4, [4, 6]],
        [[5, 6], 6, 4, [5, 4]],
        [[5, 5], 5, -4, [-4, -4]],
        [[], 1, 2, []],
        [[5, 3, 3455, 74, 74, 74, 3], 3, 20, [5, 20, 3455, 74, 74, 74, 20]],
        [[5, 3, 3455, 74, 74, 74, 3], 1, 20, [5, 3, 3455, 74, 74, 74, 3]]
    ]

    for tc in test_cases:
        print('\ttrying ' + str(tc))
        test_list = tc[0]
        output = recursion_optional.replace(test_list, tc[1], tc[2])
        ca.assert_equals(tc[3], output)
        # see if new list is a different list, even if no values are different
        ca.assert_false(output is test_list)

    print("All test cases passed for " + fn_name + "\n")



def test_remove_first():
    fn_name = inspect.stack()[0][3]
    print("Running " + fn_name)

    # Using a list because converting everything to tuples for a dictionary
    # seems too painful.
    # Format: each item is (input1, input2, answer)
    test_cases = [
        ([], 3, []),
        ([3], 3, []),
        ([3], 4, [3]),
        ([3, 4, 4, 4, 5], 4, [3, 4, 4, 5]),
        ([3, 4, 5, 4, 4, 4], 4, [3, 5, 4, 4, 4])
    ]

    for item in test_cases:
        inputlist = item[0]
        inputval = item[1]
        print('\ttrying ' + str(inputlist) + ' and ' + str(inputval))
        expected = item[2]
        ca.assert_equals(expected, recursion_optional.remove_first(inputlist,
                                                               inputval))
    print("All test cases passed for " + fn_name + "\n")



if __name__ == '__main__':

    num_run = 0
    # Tests of the optional functions
    # STUDENTS: uncomment out any tests you want to run
    for fn in [
                test_print_nested_list,
                test_embed,
                test_max_nested_list,
                test_flatten_nested_list,
                #######
                test_reverse1,
                test_reverse2,
                #######
                test_replace,
                test_remove_first,
                ]:
        fn()
        num_run += 1

    if num_run == 0:
        print("No tests were run.  Did you remember to uncomment the test functions you wanted to deploy?")
    else:
        print("*** "+str(num_run)+" tests passed. Terrific! ***")
