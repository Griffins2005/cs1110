""" 
Defines the Timer class.

A call of the form 
    Timer(x,y) 
creates a new Timer with its hours set to x its minutes to y.

Author: Lillian Lee (LJL2) and Walker White (WMW2)
Version: Feb 22 2025
"""


class Timer(object):

    """Instances represent a count-down timer having a resolution of minutes.

    Attributes:
        hours [non-negative int]: number of hours
        minutes [int in the range 0..59]: number of minutes

    """

    def __init__(self, h, m):
        """Sets this Timer's hours to h and minutes to m.

        h is a non-negative int
        m is an int in range 0..59"""
        self.hours = h
        self.minutes = m


