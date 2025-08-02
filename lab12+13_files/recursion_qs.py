"""Stubs of recursive functions for CS 1110 lab.


Author: Many CS 1110 instructors over the years.
Version: Mar 16, 2025
"""


# STUDENTS: Your functions should NOT modify its input unless the specification
# specifically mentions to do so.
from russian_doll import Doll

def even_factorial(n):
    """
    Return the product of all positive even integers up to and including n.
    In other words, n*(n-2)*(n-4)*...*2

    n: a positive even int.

    Examples:
        even_factorial(2) --> 2
        even_factorial(4) --> 8    (i.e., 4*2)
        even_factorial(6) --> 48   (i.e., 6*4*2)
    """
    # STUDENTS: leave the assertion statements in.  They will help you diagnose
    # errors.
    assert n % 2 == 0, "Halt! Received non-even input "+str(n)
    assert n >= 0, "Halt!  Received a negative input "+str(n)

    if n == 2:
         return 2
    else:
         n_product = even_factorial(n - 2)
         return n * n_product
     # STUDENTS: Implement making effective use of *recursion*.
          # (Yes, we know this can be done with a loop or even with a closed-form
          #  calculation; we're practicing recursion here.)



def sum_it(theinput):
    """Returns: Summation of all the numbers in theinput, where theinput
    can be:
        an int
        an empty list
        a list where each item is itself a valid input to this function.

    Example:
    sum_it(5) --> 5
    sum_it([5, 4]) --> 9
    sum_it([]) --> 0
    sum_it([4, [10, 11]]) -> 25
    sum_it([0, [2, 5, []], 8, [-10, -1]]) --> 4
    """
    if not theinput:
        return 0
    elif not isinstance(theinput, list):  #if not a list, it is an integer, return the integer
        return theinput
    else:
        summation = 0
        for sublist in theinput:
            summation += sum_it(sublist)
        return summation

      # STUDENTS: replace with recursive implementation.
          # You are not allowed to create a new list
          # (that is, you may not "flatten" the list).

    # Hint: since you want to do something different depending on whether
    # theinput is a list or an int, you'll want to check the result of
    # isinstance(theinput, list) or not isinstance(theinput, list)
    # of similarly with the str type.

    # Note: there are several possible approaches, including using
    # list slicing, or using a for-loop together with recursion,
    # or with `map()` (if it is covered/allowed this semester.)



def num_dolls(doll):
    """Returns: number of nesting dolls this doll contains, including itself.
    Example: if `doll` that contains one Doll in it, but that inner
    doll does not contain any Dolls, then this function returns 2.

    Precondition: doll is a Doll object (not None).
    """
    if not doll.hasSeam:     # no inner doll, return 1
        return 1

    return 1 + num_dolls(doll.innerDoll)
     # STUDENTS: implement this.


def doll_list_names(theinput):
    """Returns: list of names of the Dolls in the data structure represented
    by theinput, *sorted* in alphabetical order. Repeats should be included as
    many times as seen.

    Preconditions: theinput is either:
        a Doll (not None)
        a list (possibly empty), each element of which is a valid input
           to doll_list_names
    We assume there are no circularities in list containment.

    Examples: suppose we had:
        from russian_doll import Doll
        amy=Doll("Amy", None)
        abebe=Doll("Abebe", None)
        wei=Doll("Wei", None)
        walter=Doll("Walter", None)
        walter2=Doll("Walter", None)
        wigbert=Doll("Wigbert", None)
        thor = Doll("Thor", None)

        alist=[amy,abebe]
        wlist=[wei,walter,walter2,wigbert]
        a_and_w =[alist, wlist]
        dolls = [a_and_w, thor] # nested list
        dolls2 = [a_and_w, thor, []]

    Then, doll_list_names(dolls) -->
        ["Abebe", "Amy", "Thor", "Walter", "Walter", "Wei", "Wigbert"]
    Notice that "Walter" is there twice.

    And, doll_list_names(dolls2) -->
        ["Abebe", "Amy", "Thor", "Walter", "Walter", "Wei", "Wigbert"]
    So, the empty list in dolls2 doesn't contribute to the output.

    """
    result = []

    #If theinput is a Doll, add its name
    if isinstance(theinput, Doll):
        result.append(theinput.name)

    #If thenput is a list, process each element recursively
    elif isinstance(theinput, list):
        for item in theinput:
            result += doll_list_names(item)

    return sorted(result)
    # STUDENTS: implement this, making effective use of recursion.
          # If x is a list of strings, sorted(x) returns a new, sorted version.
          # x.sort() changes x to be sorted.
