"""

For testing functions in file funcs.py

Authors: Walker M. White (wmw2), Lillian Lee (LJL2)
Version: Feb 2025
"""

import cornellasserts
import funcs

def test_has_a_vowel():
    print('Testing function has_a_vowel')

    input = 'aeiou'
    result = funcs.has_a_vowel(input)

    cornellasserts.assert_equals(True, result)

def test_replace_first():
    """Testing function for replace_first()"""

    print("Testing funcs.replace_first")

    # 0. Given in spec: target in the middle
    result = funcs.replace_first('THanks', 'H', 'h')
    cornellasserts.assert_equals('Thanks', result)

    # 1. target at the end
    result = funcs.replace_first('CS1119', '9', '0')
    cornellasserts.assert_equals('CS1110', result)

    # 2. target at beginning
    result = funcs.replace_first('the', 't', 'T')
    cornellasserts.assert_equals('The', result)

    # 3. replace with empty string
    result = funcs.replace_first('juidge', 'i', '')
    cornellasserts.assert_equals('judge', result)

    # 4. target is same as word
    result = funcs.replace_first('Obviously', 'Obviously', 'Clearly')
    cornellasserts.assert_equals('Clearly', result)

    # 5. replacement is same as target (weird case, but not rules out by spec)
    result = funcs.replace_first('abcde', 'bc', 'bc')
    cornellasserts.assert_equals('abcde', result)

    # 6. multiple instances of target
    result = funcs.replace_first('Misissippi', 's', 'ss')
    cornellasserts.assert_equals('Mississippi', result)

    # 7. word has whitespace
    result = funcs.replace_first('eve  ning', 'e  n', 'en')
    cornellasserts.assert_equals('evening', result)

    # 8. replacement has whitespace
    result = funcs.replace_first('eveningprelim', 'gp', 'g p')
    cornellasserts.assert_equals('evening prelim', result)


    msg = "All test cases for in test_replace_first passed."
    msg = msg + "\nBut, remove or comment out any debugging print statements"
    msg = msg + " in the code being tested.\n"
    msg = msg + " If you're seeing this message,"
    msg = msg + "\nyou now have all the testing and debugging skills you need"
    msg = msg + " for A1!"
    print(msg)


#########################################
# SCRIPT CODE (Call test procedures here)

if __name__ == '__main__':
    test_replace_first()
    #test_has_a_vowel()
    print('Module funcs passed all executed tests')
    print('... but check whether any tests were actually run!')
