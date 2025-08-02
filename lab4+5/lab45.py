# lab45.py
# PUT NETID HERE
# PUT THE DATE YOU LAST CHANGED THIS FILE HERE
# Skeleton by Prof. Lee (LJL2), Feb 2 2025

"""
    Provides a time-manipulation function `change_hrs()`.

    Note: since this file is part of a lab exercise, the function may not be
    fully or correctly implemented, and may print extra diagnostic info.

"""

def change_hrs(timestr, change):
    """
    Returns the 24-hour string corresponding to updating timestr by change hours.

    The returned string is formatted as given in the preconditions for timestr.

    Additionally, this function prints information about certain key variables,
    as an aid to student debugging. This info is tab-indented.

    Preconditions on the inputs:
        timestr: A string for a 24-hour time, formatted as "hours:minutes" and obeying the following:
         No leading or trailing spaces.
         No leading zeros in the hours part, except that hours can be just "0".
         The minutes part is exactly two digits.
         Both the hours and minutes are non-negative.
         0 <= hours <= 23
         0 <= minutes <=59

        change: An int (can be 0 or negative)
    """

    ####### hours_int section starts ######
    hours_int = int(timestr.split(":")[0])  # Extract hours as int
    ####### hours_int section ends ######

    ####### new_hours_int section starts ######
    new_hours_int = (hours_int + change) % 24 # Adjust hours and ensure within 24-hour format
    ####### new_hours_int section ends ######
    minutes_part = timestr[timestr.index(":"):]  # Extract the minutes part, including the colon
    outstr = str(new_hours_int) + minutes_part
    ######## Print diagnostic info ########

    # Print some diagnostic info for students
    for var in ['timestr', 'change', 'hours_int', 'new_hours_int', 'outstr']:
        report = f'\t{var} has value ' + repr(locals()[var])
        report = report + f', type {pretty_class(locals()[var])}'
        print(report)
    print()

    return outstr  # STUDENTS: leave this line alone!


def pretty_class(x):
    """Returns string of type of x in cleaner format than type(x) does"""
    s = str(type(x))
    return s[8:s.index("'",9)]
