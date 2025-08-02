"""
Provides a function for creating the "addition" of two Timers.

Author:
  Skeleton by Walker White (wmw2), Lillian Lee (LJL2), Mar 2021
Version: Feb 22 2025
"""

# The next line means we write `Timer` instead of `timer.Timer` to
# access the Timer class from module `timer`.
from timer import Timer

def add_timers(timer1, timer2):
    """Returns: A new Timer object representing the sum of the times in
    timer1 and timer2.  Does not alter timer1 or timer2.

    Example: if timer1 represents 1 hr 59 min and timer2 represents 1 hr 2 min,
    then the **new** returned Timer represents 3 hr 1 min.

    timer1: a Timer object
    timer2: a Timer object"""
    # PLACEHOLDER: REPLACE WITH YOUR IMPLEMENTATION.
    total_minutes = timer1.minutes + timer2.minutes
    extra_hours = total_minutes // 60  #extra hours from minutes
    remaining_minutes = total_minutes % 60    #remaining minutes after overflow

    total_hours = timer1.hours + timer2.hours + extra_hours

    return Timer(total_hours, remaining_minutes)
