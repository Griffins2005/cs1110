"""
Testing functions for timer_fns.py

Author: Lillian Lee (LJL2) and Walker White (WMW2)
Version: Feb 23 2025
"""

# The next line means we write `Timer` instead of `timer.Timer` to
# access the Timer class from module `timer`. 
from timer import Timer
import timer_fns
import cornellasserts


##### TEST PROCEDURES
def print_info(t1, t2):
    """Prints
    '\tTesting Timer (<t1h>, <t1m>) and Timer (<t2h>, <t2m>)'

    where t1 has hours t1h and minutes t1m,
    t2 has hours t2h and minites t2m
    
    t1 and t2 are Timer objects
    """
    msg = '\tTesting Timer('+str(t1.hours)+", "+str(t1.minutes)
    msg = msg + ') and Timer ('+str(t2.hours)+", "+str(t2.minutes) + ')'   
    print(msg)


def test_add_time():
    print("Running test_add_timer")

    t1 = Timer(1,59)
    t2 = Timer(1,2)
    print_info(t1, t2)
    sum_timer = timer_fns.add_timers(t1,t2)
    # Check types are as expected
    cornellasserts.assert_equals(True, isinstance(sum_timer, Timer))
    cornellasserts.assert_equals(True, isinstance(t1, Timer))
    cornellasserts.assert_equals(True, isinstance(t2, Timer))
    # Check result of adding is correct
    cornellasserts.assert_equals(3, sum_timer.hours)
    cornellasserts.assert_equals(1, sum_timer.minutes)
    # Check that input Timers weren't changed
    cornellasserts.assert_equals(1, t1.hours)
    cornellasserts.assert_equals(59, t1.minutes)
    cornellasserts.assert_equals(1, t2.hours)
    cornellasserts.assert_equals(2, t2.minutes)

    t1 = Timer(11,59)
    t2 = Timer(13,59)
    print_info(t1, t2)
    sum_timer = timer_fns.add_timers(t1,t2)
    cornellasserts.assert_equals(True, isinstance(sum_timer, Timer))
    cornellasserts.assert_equals(True, isinstance(t1, Timer))
    cornellasserts.assert_equals(True, isinstance(t2, Timer))
    cornellasserts.assert_equals(25, sum_timer.hours)
    cornellasserts.assert_equals(58, sum_timer.minutes)
    cornellasserts.assert_equals(11, t1.hours)
    cornellasserts.assert_equals(59, t1.minutes)
    cornellasserts.assert_equals(13, t2.hours)
    cornellasserts.assert_equals(59, t2.minutes)    

    t1 = Timer(1,50)
    t2 = Timer(0,2)
    print_info(t1, t2)
    sum_timer = timer_fns.add_timers(t1,t2)
    cornellasserts.assert_equals(True, isinstance(t1, Timer))
    cornellasserts.assert_equals(True, isinstance(t2, Timer))
    cornellasserts.assert_equals(True, isinstance(sum_timer, Timer))
    cornellasserts.assert_equals(1, sum_timer.hours)
    cornellasserts.assert_equals(52, sum_timer.minutes)
    cornellasserts.assert_equals(1, t1.hours)
    cornellasserts.assert_equals(50, t1.minutes)
    cornellasserts.assert_equals(0, t2.hours)
    cornellasserts.assert_equals(2, t2.minutes)

    print("Finished test_add_timer")

# CODE TO EXECUTE

print("Beginning tests of timer_fns code")
test_add_time()
print("All test cases for timer_fns passed. Time(r) to celebrate!")
