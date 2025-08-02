"""

Demonstrating a simple call to cornellasserts.py

Authors: Walker White (WMW2) and Lillian Lee (LJL2)
Version: Feb 9 2025
"""

import cornellasserts


def test_asserts():
    """
    Demonstrates cornellasserts.assert_equals()
    """
    print('Running cornellasserts asserts...')
    cornellasserts.assert_equals('b c', 'ab cd'[1:4])
    cornellasserts.assert_equals('b c', 'ab cd'[1:3])


#########################################
# SCRIPT CODE (Call test procedures here)
if __name__ == '__main__':
    test_asserts()
    print('All tests passed.')
