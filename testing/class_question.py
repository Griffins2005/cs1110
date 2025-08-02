class Date:
    """Objects represent an instance of a Date.

    Class attributes:
         MAX_DAYS: 31, the maximum number of days that any month can have

    Instance attributes:
          month [str]: 3-character, uppercase abbreviation of the month
          day [int]: the day of the month, 0 < day <= MAX_DAYS for a Date   """


    def __init__(self, m, d):
        """ Creates a new Date with attributes set as follows:
               month: the first 3 characters of m, uppercase
               day: set to d, **OR** the max legal value if d is too large

        Preconditions:  (STUDENTS: don't assert them)
            m: a str with len >= 3
            d: an int, 0 < d        """

    def __eq__(self, other):
        """ Returns: True if the month and day of the Dates are equal, 
        False o.w.
        Precondition (no need to assert):   other is a Date.      """




class Holiday:
    """ Objects represent an instance of a holiday.

    Attributes:
        name [non-empty str]: the name of this holiday
        start [Date]: the date that this holiday begins
        duration [int]: how many days this holiday lasts        """

    def __init__(self, n, start, stop=None):
        """Creates a new holiday with attributes set as follows:
            * name: set to `n`
            * start [Date]: set to `start`
            * duration: set to the length of the holiday, given the start and
                 stop Dates. Note: stop Date is an optional argument that might
                 be a Date or might have the value None.
            Preconditions (they are done for you):
                n: a str
                start: a Date
                stop: a Date in the same month as the start Date
                     or None                                         """
        assert type(n) == str, "Bad arg to __init__: n should have type str"
        assert isinstance(start,Date), "Bad arg to __init__: start should be a Date"
        assert (stop is None) or isinstance(stop,Date), "Bad arg to __init__: stop should be None or a Date but is "+repr(stop)
        if isinstance(stop,Date):
            assert start.month == stop.month, "Bad arg to __init__: start and stop should be in the same month"


def num_holidays(holiday_list):
    """Returns the number of days off, given a list of Holidays, holiday_list

    Example:

        SU22 = [Holiday("Juneteenth", Date("June", 20))]     # 1 day holiday
        num_holidays(SU22) --> returns 1

        FA21 = [Holiday("Labor Day", Date("September", 6)),         # 1 day holiday
                Holiday("Fall Break", Date("October", 9), Date("October", 12)),  # 4 day holiday
                Holiday("Thanksgiving", Date("November", 24), Date("November", 28))]  # 5 day holiday
        num_holidays(FA21) --> returns 10
    """

