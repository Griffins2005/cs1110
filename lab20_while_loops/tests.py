"""
Testing for while-loop lab

Authors: Lillian Lee (LJL2) and Walker White (wmw2)
Version: Apr 29, 2025
"""

import cornellasserts
import funcs


def test_duplicate_copy():
    """
    Tests the function duplicate_copy
    """
    print('Testing duplicate_copy')
    cornellasserts.assert_equals([5,5], funcs.duplicate_copy([5],5))
    cornellasserts.assert_equals([], funcs.duplicate_copy([], 1))
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    cornellasserts.assert_equals([5, 3, 3, 3455, 74, 74, 74, 3, 3], funcs.duplicate_copy(mylist,3))
    cornellasserts.assert_equals([5, 3, 3455, 74, 74, 74, 74, 74, 74, 3], funcs.duplicate_copy(mylist, 74))
    print('  duplicate_copy looks okay')


def test_duplicate():
    """
    Tests the function duplicate
    """
    print('Testing duplicate')
    mylist = [5]
    funcs.duplicate(mylist,5)
    cornellasserts.assert_equals([5,5], mylist)
    
    mylist = []
    funcs.duplicate(mylist,1)    
    cornellasserts.assert_equals([], mylist)
    
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    funcs.duplicate(mylist, 3)
    cornellasserts.assert_equals([5, 3, 3, 3455, 74, 74, 74, 3, 3], mylist)
    
    funcs.duplicate(mylist, 74)
    cornellasserts.assert_equals([5, 3, 3, 3455, 74, 74, 74, 74, 74, 74, 3, 3], mylist)
    print('  duplicate looks okay')


def test_exp():
    """
    Tests the function exp
    """
    print('Testing exp')
    cornellasserts.assert_equals(2.71828,      round(funcs.exp(1),5))
    cornellasserts.assert_equals(2.71828182846,round(funcs.exp(1,1e-12),11))
    cornellasserts.assert_equals(0.13534,      round(funcs.exp(-2),5))
    cornellasserts.assert_equals(0.13533528324,round(funcs.exp(-2,1e-12),11))
    cornellasserts.assert_equals(2981.0,       round(funcs.exp(8,1e-1),0))
    cornellasserts.assert_equals(2980.95799,   round(funcs.exp(8),5))
    cornellasserts.assert_equals(2980.95798704173,round(funcs.exp(8,1e-12),11))
    print('  exp looks okay')


# Script Code
if __name__ == '__main__':
    test_duplicate_copy()
    test_duplicate()
    test_exp()
    
    print('The module funcs passed all tests')

