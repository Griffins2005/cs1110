# clamp_test.py
# L.  Lee (LJL2), W. White (wmw2)
# March 2021

import clamp as clamp_module


def test_clamp():

    print("Starting function test_clamp()")

    # We use tuples temporarily to encode our testcases
    # because dictionaries can't handle lists as keys.
    testcases = {((-1, 1, 3, 5), 0, 4): [0, 1, 3, 4],
             ((1, 3), 0, 4): [1,3],
             ((-1, 1, 3, 5), 1, 1): [1, 1, 1, 1],
             ((5, 0, 2, 7, 4), 0, 4.5):[4.5, 0, 2, 4.5, 4],
             ((5, 0, 1, 7, 4), 0.5, 4): [4, 0.5, 1, 4, 4],
             ((), 0, 4): [],
             ((-1, -1, -1, 5), 0, 3): [0, 0, 0, 3]
             }

    for tc in testcases:
        thelist = list(tc[0])
        m1 = tc[1]
        m2 = tc[2]
        expected = testcases[tc]

        msg = "\ttesting list " + str(thelist) + ", floor: " + str(m1)
        msg += ", " + " ceiling: " + str(m2)
        print(msg)

        returned = clamp_module.clamp(thelist, m1, m2)
        assert returned is None, \
            "Problem: clamp() shouldn't return anything, but it returned "+ repr(returned)

        assert len(thelist) == len(expected), \
            "Problem: clamp() changed the length of the list"

        for i in range(len(expected)):
            assert expected[i] == thelist[i], \
                "Problem with item at index i. Was " +repr(thelist[i]) + " but should have been " + repr(expected[i])

        print("\tTest passed.")

    print("Done with test_clamp()")


def test_outliers():
    print("Starting function test_outliers()")
    # We use tuples temporarily to encode our testcases
    # because dictionaries can't handle lists as keys.
    testcases = {((-1, 1, 3, 5), 0, 4): [0, 3],
             ((1, 3), 0, 4): [],
             ((-1, 1, 3, 5), 1, 1): [0, 2, 3],
             ((5, 0, 2, 7, 4), 0, 4.5):[0, 3],
             ((5, 0, 1, 7, 4), 0.5, 4): [0, 1, 3],
             ((), 0, 4): [],
             ((-1, -1, -1, 5), 0, 3): [0, 1, 2, 3] # repeats in alist ...
             }
    for tc in testcases:
        thelist = list(tc[0])
        m1 = tc[1]
        m2 = tc[2]
        expected = testcases[tc]
        orig = thelist[:]

        msg = "\ttesting list " + str(thelist) + ", floor: " + str(m1)
        msg += ", " + " ceiling: " + str(m2)
        print(msg)

        returned = clamp_module.outliers(thelist, m1, m2)
        assert returned == expected, \
            "Problem: Expected "+str(expected)+" but got "+str(returned)

        assert thelist == orig, \
            "Problem: input list should not have been changed, but was."

    print("Done with test_outliers()")

if __name__ == '__main__':
    test_clamp()
    test_outliers()
    print("All tests finished without problems!  Huzzah!")

