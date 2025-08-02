# greetings.py
# PUT YOUR NETID HERE (not your name)
# PUT DATE OF LAST CHANGE HERE
# Skeleton by Prof L. Lee, Jan 2025

"""Library of functions producing greetings"""

import random
def natural_hi():
    """
    Documentation omitted for lab exercise purposes.
    """

    user_name = input('Please enter your name: ')
    reps = random.randint(1,15)
    return "hi "*reps + user_name + "!"
