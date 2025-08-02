"""

Lab exercise on raising exceptions.

Authors:
    Stub: Walker White (wmw2) and Lillian Lee (LJL2)
Version: Apr 8, 2025

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
    # STUDENTS: You might find the method s.isdigit() mentioned
    # in the preamble to the previous activity to be useful.
