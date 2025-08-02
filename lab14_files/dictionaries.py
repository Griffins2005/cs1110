"""
Functions involving dictionaries.

Author:
    Initial skeleton by W. White (wmw2)
    Cuts, minor edits, alternate solutions by Lillian Lee (LJL2)
Version: Mar 23 2025
"""




def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student, given
    a dictionary with numerical scores.

    The dictionary adict has keys that are netids (strings) and
    values that are ints 0-100.

    The function returns a new dictionary with netids for keys and letter grades
    (strings) for values.  The cut-off is 90 for an A, 80 for a B, 70 for a C,
    60 for a D.  Anything below 60 is an F.

    Example:  letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.

    Parameter adict: the dictionary of scores.
    Precondition: adict is a dictionary with string keys, int values
    """
    # STUDENTS:Implement here. Your solution must be fundamentally based on
    # for-loops over dictionaries. (And, no dictionary comprehensions are allowed.)
    # HINT: Start with empty accumulator dictionary = {} and add to it.
    #
    # CHALLENGE: We wrote a solution with no if-statements! Can you?
    # We used an additional dictionary and the floor-division operator //
    grades = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}  # use tens place in scores
    result = {}

    for (netid, score) in adict.items():
        result[netid] = grades.get(score // 10, 'F') #F is default if key not found
    return result


def convert_grades(adict):
    """
    Modifies the dictionary to replace numerical scores with letter grades.

    The dictionary adict has keys that are netids (nonempty strings) and
    values that are ints 0-100.

    This function replaces all numerical grades with letter grades (strings)
    for values. Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for
    a D. Anything below 60  is an F.

    Parameter adict: the dictionary of scores
    Precondition: adict is dictionary mapping strings to ints


    Example: If a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}, letter_grades(a)
             changes a to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
    Example: If a = {}, letter_grades(a) changes a to {}


    """
    grades = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}

    for key in adict:
        adict[key] = grades.get(adict[key] // 10, 'F')
    # STUDENTS: Implement me.  Your solution must be fundamentally based on
    # for-loops over dictionaries. (And, no dictionary comprehensions are allowed.)

### OPTIONAL EXERCISES ###



def average_grade(adict):
    """
    Returns the average score among all students.

    The dictionary adict has keys that are netids (nonempty strings) and
    values that are ints 0-100.

    Parameter adict: the dictionary of grades
    Precondition: adict is a dictionary with string keys, int values


    Example: letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to (55+90+86)/3 = 77.
    """
    count = 0
    average = 0

    for score in adict.values():
        if count == 0:
            if len(adict) == 0:
                return 0
        count += 1
        average += (score - average) / count

    return average
    # STUDENTS: Implement here. Your solution must be fundamentally based
          # on for-loops over dictionaries. You may not use sum().
