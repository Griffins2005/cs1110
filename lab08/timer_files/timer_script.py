""" 
Example of working with Timers

Author: Lillian Lee (LJL2)
Version: Feb 22 2025
"""

from timer import Timer # Make name `Timer` directly available
                        # (replaces expressions like `timer.Timer`)

t = Timer(2,30)
s = t  # This is like grouping two students on CMS, 
       # linking their deadlines
t.minutes = 20
print("t.minutes is: " + str(t.minutes))
print("s.minutes is: " + str(s.minutes))
print()

s = Timer(t.hours, t.minutes)  
# The above is like un-grouping two students on CMS,
# by making each student have their own deadline.
# So their deadlines are no longer *linked*, even
# though they currently have the same values.

print("t.minutes is: " + str(t.minutes))
print("s.minutes is: " + str(s.minutes)) 
print()

t.minutes = 10
print("t.minutes is: " + str(t.minutes))
print("s.minutes is: " + str(s.minutes))
