"""
A module devoted to while-loops

Author: Walker White (WMW2) and Lillian Lee (LJL2)
Version: Apr 27, 2025
"""


# REQUIRED FUNCTIONS
def duplicate_copy(nums, a):
    """
    Returns a COPY of nums but with all occurrences of `a` duplicated

    Examples: duplicate_copy([1,2,3,1], 1) returns [1,1,2,3,1,1].
              duplicate_copy([1,2,3,1], 4) returns [1,2,3,1].
              duplicate_copy([1,1], 1) returns [1,1,1,1].

    Parameter nums: list to copy
    Precondition: nums is a list of ints

    Parameter a: value to search for
    Precondition: `a` is an int
    """
    results = []
    i = 0
    while i < len(nums):
        results.append(nums[i])
        if nums[i] == a:
            results.append(nums[i])
        i += 1
    return results

      # STUDENTS: implement with a while-loop


def duplicate(nums, a):
    """
    Modifies thelist so that all occurrences of `a` are duplicated

    Does not return anything.

    Examples: If nums is [1,2,3,1] then nums becomes [1,1,2,3,1,1] after duplicate(nums,1).
              If nums = [1,2,3,1] then nums remains [1,2,3,1] after duplicate(nums, 4).

    Parameter nums: list to modify
    Precondition: nums is a list of ints

    Parameter a: value to search for
    Precondition: `a` is an int
    """
    i = 0
    while i < len(nums):
        if nums[i] == a:
            # insert a copy immediately after the current position
            nums.insert(i+1, a)
            # skip past both the original and the inserted copy
            i += 2
        else:
            i += 1

      # STUDENTS: implement with a while-loop
          # For the purposes of this lab, you are *not* allowed
          # to create a new list as part of solving this problem;
          # you must use list method insert() to insert new values
          # directly into nums instead.
          # Instead, think carefully about how your loop variable
          # should be adjusted as the length of the list changes.


# count_inputs() must be tested manually
def count_inputs():
    """
    Returns the number of times the user chose to continue.

    This function repeated asks the user

        Keep going [y/n]?

    If the user answers 'y', the function adds one to a counter and keeps going.
    If the user answers 'n', the function quits and returns the number of times
    that the user answered 'y'.  If the user answers anything else, the function
    responds with

        Answer unclear. Use 'y' or 'n'.

    It will not quit in this case, but it will not add to the counter either.
    """
    # STUDENTS: implement this function.
    # We suggest you use the following strategy:
    # Create a counter accumulator
    # Create a variable `going` to control the loop
    # While the user has not told us to stop
        # Get the input from the user
        # Respond with error message if input is bad
        # Update counter if input is 'y'
    count = 0
    going = True
    while going:
        answer = input('Keep going [y/n]?')
        if answer == 'y':
            count += 1
        elif answer == 'n':
            going = False
        else:
            print("Answer unclear. Use 'y' or 'n'.")
    return count



# OPTIONAL FUNCTION
def exp(x, err=1e-6):
    """
    Returns the value of (e ** x) to with the given margin of error.

    The value (e ** x) is given by the Power Series

        1 + x + (x ** 2)/2 + (x ** 3)/3! + ... + (x ** n)/ n! + ...

    We cannot add up infinite values in a program.  So we approximate (e ** x)
    by choosing a value n and stopping at that:

        1 + x + (x ** 2)/2 + (x ** 3)/3! + ... + (x ** n)/ n!

    The error of this approximation is

        abs( (x ** (n+1))/(n+1)!)

    which we want less than err.  So to compute e ** x, we just keep computing
    term = (x ** n)/ n! in a loop until this value is less than our error.  If it
    is not less than the error, we add it to the accumulator, which we return at
    the end.

    Hint: (x**(n+1))/(n+1)!  == (x**n)/n! * x/(n+1)
    Use this fact to simplify your loop.

    Parameter x: the exponent for e ** x
    Precondition: x is a numbers

    Parameter err: The margin of error (OPTIONAL: default is e-6)
    Precondition: err > 0 is a number
    """
    # STUDENTS: If optional parameters have not been covered this
    # semester: the `err=1e-6` in the function header means that if
    # caller doesn't supply an `err` argument, the function will
    # automatically create a variable `err` with value `1e-6`.

    approx = 0.0  # Approximation of e ** x
    term   = 1.0  # 1 is the first term in the Power Series
    n = 0         # term 1 corresponds to (x ** 0)/0!

    # STUDENTS: complete the rest of this function,
    # making your implementation based on a while-loop.
    # You may not simply return  (math.e ** x);  in fact,  this
    # function should compute a more accurate approximation.
    # Don't forget to return `approx`.
    # keep adding terms until the next term is smaller than err
    while abs(term) >= err:
        approx += term
        # add the current term Tₙ to our running total

        # compute Tₙ₊₁ efficiently from Tₙ:
        term = term * x / (n + 1)
        # multiply by x and divide by (n+1) to get x^(n+1)/(n+1)!

        n += 1
        # move to the next term index

    return approx
    # once the loop finishes, approx is within err of the true e**x
