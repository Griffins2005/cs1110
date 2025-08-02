"""
Tests for dictionary-based functions. 

Author: Walker M. White (wmw2)
Version:   October 20, 2021
"""
import cornellasserts
import dictionaries
import copy


def test_letter_grades():
    """
    Test procedure for function letter_grades
    """
    print('Testing function letter_grades')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]
    actual = ['F',    'A',      'B',     'C',     'A',       'D',     'C'    ]


    inputs = {'wmw2': 55}
    result = dictionaries.letter_grades(inputs)
    expected_result = {'wmw2': 'F'}
    cornellasserts.assert_equals(expected_result, result)
    original_input = {'wmw2': 55}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90}
    result = dictionaries.letter_grades(inputs)
    expected_result = {'wmw2': 'F', 'abc123': 'A'}
    cornellasserts.assert_equals(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85}
    result = dictionaries.letter_grades(inputs)
    expected_result = {'wmw2': 'F', 'abc123': 'A', 'jms45': 'B'}
    cornellasserts.assert_equals(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72}
    result = dictionaries.letter_grades(inputs)
    expected_result = {'wmw2': 'F', 'abc123': 'A', 'jms45': 'B', 'qoz15': 'C'}
    cornellasserts.assert_equals(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100}
    result = dictionaries.letter_grades(inputs)
    expected_result = {'wmw2': 'F', 'abc123': 'A', 'jms45': 'B', 'qoz15': 'C', 'xyz2345': 'A'}
    cornellasserts.assert_equals(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100, 'jms46': 63}
    result = dictionaries.letter_grades(inputs)
    expected_result = {'wmw2': 'F', 'abc123': 'A', 'jms45': 'B', 'qoz15': 'C', 'xyz2345': 'A', 'jms46': 'D'}
    cornellasserts.assert_equals(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100, 'jms46': 63}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified


def test_convert_grades():
    """
    Test procedure for function convert_grades.
    """
    print('Testing function convert_grades')

    grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
    answer = {'wmw2': 'F', 'abc3': 'A', 'jms45': 'B'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50}
    answer = {'abc123': 'F','abc456':'D','jms457':'F'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,'xyz456':80,'wmw4':90}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C','xyz456':'B','wmw4':'A'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
              'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
              'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A','tor3':'B'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {'wmw2' : 55, 'abc3' : 90}
    answer = {'wmw2' : 'F', 'abc3' : 'A'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {'abc3' : 90}
    answer = {'abc3' : 'A'}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)

    grades = {}
    answer = {}
    result = dictionaries.convert_grades(grades)
    cornellasserts.assert_equals(None,result)
    cornellasserts.assert_equals(answer,grades)



### OPTIONAL EXERCISES ###

def test_average_grade():
    """
    Test procedure for function average_grade
    """
    print('Testing function average_grade')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]
    run_avg =[55.0, 72.5, 76.66666666666667, 75.5, 80.4, 77.5, 77.42857142857143]


    inputs = {'wmw2': 55}
    result = dictionaries.average_grade(inputs)
    expected_result = 55.0
    cornellasserts.assert_floats_equal(expected_result, result)
    original_input = {'wmw2': 55}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90}
    result = dictionaries.average_grade(inputs)
    expected_result = 72.5
    cornellasserts.assert_floats_equal(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85}
    result = dictionaries.average_grade(inputs)
    expected_result = 76.66666666666667
    cornellasserts.assert_floats_equal(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72}
    result = dictionaries.average_grade(inputs)
    expected_result = 75.5
    cornellasserts.assert_floats_equal(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100}
    result = dictionaries.average_grade(inputs)
    expected_result = 80.4
    cornellasserts.assert_floats_equal(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100, 'jms46': 63}
    result = dictionaries.average_grade(inputs)
    expected_result = 77.5
    cornellasserts.assert_floats_equal(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100, 'jms46': 63}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified

    inputs = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100, 'jms46': 63, 'jms47': 77}
    result = dictionaries.average_grade(inputs)
    expected_result = 77.42857142857143
    cornellasserts.assert_floats_equal(expected_result, result)
    original_input = {'wmw2': 55, 'abc123': 90, 'jms45': 85, 'qoz15': 72, 'xyz2345': 100, 'jms46': 63, 'jms47': 77}
    cornellasserts.assert_equals(original_input, inputs)  # Check unmodified


# Script code
if __name__ == '__main__':
    test_letter_grades()
    test_convert_grades()
    print("Your code passed all required tests. That's great in our book!\n\n")

    test_average_grade()
    print("Your code passed all required and optional tests. Excellent DICTion!")
