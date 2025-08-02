# lab45_test.py
# Prof. Lee (LJL2)
# Feb 2025


""" Provides function for testing lab45 functions. """

import lab45  # change_hr() is in lab45 module
import cornellasserts  #  useful code-checking functions



def run_change_hrs(run_all):
    """Run lab45.py change_hr function on various inputs, printing diagnostics.

        If run_all is False, halts on the first test case that fails.
        If run_all is True, all test cases are run, but the user needs to
            read all the output to check for errors.

        Precondition: run_all is a boolean
    """

    # Throughout, we use the function `repr()` so that if `result` is a string,
    # the output of `print(repr(result))` will show quotation marks around it;
    # ordinarily, `print()` does not display quote marks around its output.
    #
    # Example: if n is the int 5 and s is the string "5"
    # print(n) -> 5
    # print(repr(n)) -> 5
    # print(s) -> 5
    # print(repr(s)) -> '5'

    scratch = "Your program works on all our test cases! "
    msg_if_error = '*** Oops, mismatch somewhere above!  Find and fix the problem, then re-test.'
    d = False # throwaway variable

    print('\n')
    print("Trying input '9:04' and 5")
    result = lab45.change_hrs('9:04', 5)
    print("Function returned: " + repr(result))
    correct_answer = '14:04'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '9:04' and -5")
    result = lab45.change_hrs('9:04', -5)
    print("Function returned: " + repr(result))
    correct_answer = '4:04'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '9:04' and -10")
    result = lab45.change_hrs('9:04', -10)
    print("Function returned: " + repr(result))
    correct_answer = '23:04'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '9:04' and -36")
    result = lab45.change_hrs('9:04', -36)
    print("Function returned: " + repr(result))
    correct_answer = '21:04'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")


    print("Trying input '9:04' and 0")
    result = lab45.change_hrs('9:04', 0)
    print("Function returned: " + repr(result))
    correct_answer = '9:04'
    print("Correct answer   : " + repr(correct_answer))
    scratch+="It's happy hour!!"
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '22:13' and 5")
    result = lab45.change_hrs('22:13', 5)
    print("Function returned: " + repr(result))
    correct_answer = '3:13'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '22:13' and -24")
    result = lab45.change_hrs('22:13', -24)
    print("Function returned: " + repr(result))
    correct_answer = '22:13'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '22:13' and 49")
    result = lab45.change_hrs('22:13', 49)
    print("Function returned: " + repr(result))
    correct_answer = '23:13'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '0:00' and 1")
    result = lab45.change_hrs('0:00', 1)
    print("Function returned: " + repr(result))
    correct_answer = '1:00'
    print("Correct answer   : " + repr(correct_answer))
    d= run_all or cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n")

    print("Trying input '0:00' and -2")
    result = lab45.change_hrs('0:00', -2)
    print("Function returned: " + repr(result))
    correct_answer = '22:00'
    print("Correct answer   : " + repr(correct_answer))
    # RUN the last assert_equals regardless of value of `all`
    cornellasserts.assert_equals(correct_answer, result, msg_if_error)
    print("\n"+scratch)

# MAIN CODE FOR RUNNING THE TESTS

msg = "This is lab45_test.py, declaring that I have been called successfully."
print(msg)

halt_mode = True  # if True, stops at first mismatch
                  # if False, user needs to eyeball output to see mismatches

run_change_hrs(not halt_mode)
