"""

Tests for try_except_file_input.py

Author: Lillian Lee (LJL2) and Walker White (wmw2)
Version: Apr 13 2025

"""
import try_except_file_input as labfile
import cornellasserts
import sys # to raise a SystemExit

def test_time_to_military():
    print("begin test_time_to_military")

    goodtests = [('9:05 AM','09:05'),('11:05 AM','11:05'),('9:05 PM','21:05'),('11:05 PM','23:05'),('12:00 PM','12:00'), ('12:00 AM','00:00')]

    for test_case in goodtests:
        test_in = test_case[0]
        expected = test_case[1]

        try: 
            result = labfile.time_to_military(test_in)
        except Exception as e:
            print('Unexpected Error occurred on input '+ test_in+": "+str(e))
            sys.exit()

        assert expected == result, \
            'Input ' + repr(test_in) + ' gave incorrect output '+repr(result)

    bad_inputs = [956, 'abc', '9:05', '2:60 PM', '0:12 AM', '02:45 PM', '7:4 AM', '14:45']

    for test_in in bad_inputs:
        try: 
            result = labfile.time_to_military(test_in)
        except Exception as e:
            print('Unexpected Error occurred on input '+ test_in+": "+str(e))
            sys.exit()

        assert result == 'Invalid time format', \
            'Input ' + repr(test_in) + ' gave incorrect output '+repr(result)

    print("finished test_time_to_military. Seems like you had a good TIME!")


def test_get_one_less():
    """
    Tests the get_one_less function
    """
    print('Testing the function get_one_less')

    cornellasserts.assert_equals(22,  labfile.get_one_less('file_good.txt'))
    cornellasserts.assert_equals('ABC',labfile.get_one_less('file_bad.txt'))
    cornellasserts.assert_equals(None, labfile.get_one_less('file_huh.txt'))

    print('Finished testing get_one_less')


if __name__ == '__main__':
    msg = 'Disclaimer: this testing code does not check time_to_military() for'
    msg += ' try, except, or if-statements\n'
    print(msg)
    test_time_to_military()
    test_get_one_less()
    print("All our tests passed.")