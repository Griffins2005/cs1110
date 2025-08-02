"""

Functions to exercise exceptions, try/accept, and reading from a file.

Authors:
    Stub: Walker White (wmw2) and Lillian Lee (LJL2)
Version: Apr 13, 2025

"""
def time_format_check(s):
    """
    Returns: True if s is a string in proper 12-hour format <hours>:<mins> AM/PM.

    Proper 12-hour format includes:
    no leading zero in <hours> but <mins> should have a leading zero if there
    are 9 or fewer minutes.

    Raises a TypeError if s is not a string.

    Raises a ValueError if s is a string but is not in proper 12-hour format.

    Parameter s: the candidate time to format
    Precondition: NONE (s can be any value)

    Examples:
        time_format_check('2:45 PM') returns True
        time_format_check('2:45PM') --> ValueError
        time_format_check('14:45')  --> ValueError
        time_format_check('14:45 AM')  --> ValueError
        time_format_check(245)  --> TypeError

    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    parts = s.split(' ')
    if len(parts) != 2:
        raise ValueError("Time must contain a space between time and AM/PM")

    time_part, period = parts

    if period not in ('AM', 'PM'):
        raise ValueError("Time must end with 'AM' or 'PM'")

    if ':' not in time_part:
        raise ValueError("Time must contain a colon between hours and minutes")

    hour_min = time_part.split(':')
    if len(hour_min) != 2:
        raise ValueError("Time must be in the format <hour>:<minutes>")

    hour_str, min_str = hour_min

    if not hour_str.isdigit() or not min_str.isdigit():
        raise ValueError("Hour and minutes must be numeric")

    hour = int(hour_str)
    minute = int(min_str)

    if hour < 1 or hour > 12:
        raise ValueError("Hour must be between 1 and 12 (no leading zero allowed)")

    # Ensure no leading zero in hour
    if hour_str != str(hour):
        raise ValueError("Hour must not have a leading zero")

    if minute < 0 or minute > 59:
        raise ValueError("Minute must be between 00 and 59")

    # Leading zero check for minutes
    if minute < 10 and len(min_str) != 2:
        raise ValueError("Minutes less than 10 must have a leading zero")

    return True
    # STUDENTS: copy in your code from time_check.py in the previous lab.



def time_helper(s):
    """
    Returns: a string representing the time in 24-hour (military) format.

    24-hour format has the form '<hours>:<minutes>'.
    The hours are between 0 and 23 inclusive, and are always two digits, meaning
    that a leading zero should be added when appropriate.
    The minutes are between 0 and 59 inclusive, and are always 2 digits.

    Examples:
        time_helper('2:45 PM') returns '14:45'
        time_helper('9:05 AM') returns '09:05'
        time_helper('12:00 AM') returns '00:00'

    param str s:  a string in 12-hour format <hours>:<min> AM/PM, with no
    leading zeros for the <hours> part, but leading zeros are allowed in the <min>
    part.
    """
    # Step 1: Split input into time part and period
    time, period = s.split()

    # Step 2: Split time into hours and minutes
    hour, minute = time.split(':')
    hour = int(hour)
    minute = int(minute)

    # Step 3: Convert hour based on AM/PM
    if period == "AM":
        if hour == 12:
            hour = 0  # Special case for 12 AM (midnight)
    elif period == "PM":
        if hour != 12:
            hour += 12  # Add 12 to convert PM to 24-hour format

    formatted_hour = str(hour)
    formatted_minute = str(minute)

    if hour < 10:
        formatted_hour = "0" + formatted_hour
    if minute < 10:
        formatted_minute = "0" + formatted_minute

    return formatted_hour + ":" + formatted_minute

def time_to_military(s):
    """
    Returns: a string representing the time in 24-hour (military) format, or
    'Invalid time format' is the input isn't properly formatted.

    24-hour format has the form '<hours>:<minutes>'.
    The hours are between 0 and 23 inclusive, and are always two digits, meaning
    that a leading zero should be added when appropriate.
    The minutes are between 0 and 59 inclusive, and are always 2 digits.

    If input `s` is not a string in 12-hour format as described in item (1) of
    the precondition below, then the string 'Invalid time format' is returned.

    Examples:
        time_to_military('2:45 PM') returns '14:45'
        time_to_military('9:05 AM') returns '09:05'
        time_to_military('12:00 AM') returns '00:00'
        time_to_military(905) returns 'Invalid time format'
        time_to_military('abc') returns 'Invalid time format'
        time_to_military('9:05') returns 'Invalid time format'

    Parameter str s: Either:
    (1) s is a string in 12-hour format <hours>:<min> AM/PM, with no
    leading zeros for the <hours> part, but leading zeros are allowed in the <min>
    part, or
    (2) s is not such a string.
    """
    try:
         #Check if the input is a valid time format
        time_format_check(s)

        #Convert time to military time format
        return time_helper(s)

    except (TypeError, ValueError):
        return 'Invalid time format'
      # STUDENTS:
          # You must use try/except, instead of if-statements.
          # In order to avoid using if-statements, we add the following requirements:
          # You must use time_format_check() as a helper.
          # You must use time_helper() as a helper.



def get_one_less(filename):
    """
    Returns the int that is one less than the int stored in `filename`.

    If the file does not contain an int, this function returns the contents of the file.

    If the file does not exist or cannot be opened, this function returns None.

    Parameter filename: The name of the file to open
    Precondition: filename is a string
    """
    try:
        # Open the file and read its content
        with open(filename) as file:
            content = file.read()

        # Attempt to convert content to integer and subtract one
        return int(content) - 1
    except ValueError:
        # If the content is not an integer, return the content itself
        return content
    except FileNotFoundError:
        # If the file does not exist, return None
        return None
     # STUDENTS: No if-statements allowed.
          # Hint: int(x) raises a ValueError if x is not an int
