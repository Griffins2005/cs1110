"""

Tests for is_time_format

Author: Lillian Lee (LJL2), missing test case added by Adeniyi Fagbewesa (AMF349)
Version: Apr 9 2025

"""

import cornellasserts
import time_check

def test_time_format_check():
    print("begin test")

    result = time_check.time_format_check('2:45 PM')
    cornellasserts.assert_equals(True, result)

    result = time_check.time_format_check('11:59 AM')
    cornellasserts.assert_equals(True, result)

    for badtype in (1, 0, True, False, ['a', 'b']):
        try:
            result = time_check.time_format_check(badtype)
            assert False, "Unexpectedly, no Exception raised for "+repr(badtype)  
        except TypeError:
            pass # We are expecting a TypeError
                      

    for badstring in ('2:45PM', '14:45', '14:45 AM', '11:45AM', '2:60 PM', '0:12 AM', '7:4 AM', '02:45 PM'):
        try:
            result = time_check.time_format_check(badstring)
            assert False, "Unexpectedly, no Exception raised for "+repr(badstring)
        except ValueError:
            pass # We are expecting a ValueError



    print("We didn't detect any problems.  You've raised the bar!")

if __name__ == '__main__':
    test_time_format_check()