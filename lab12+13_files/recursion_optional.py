# recursion_optional.py
# YOUR NETID HERE
# THE DATE COMPLETED HERE
# April 2021
# Skeleton by various CS1110 profs over the years

"""Optional additional recursion exercises.
   See accompanying file for some test cases.

   Table of contents (search for these comments in the file)

    ##### FUNCTIONS WHERE RECURSION IS "NATURAL" ########

    ##### FUNCTIONS WHERE FOR-LOOPS OR OTHER MECHANISM WOULD BE MORE "NATURAL", BUT
    ##### THERE IS AN INTERESTING RECURSION IDEA ALSO

    ##### FUNCTIONS WHERE FOR-LOOPS OR OTHER MECHANISM WOULD BE MORE "NATURAL", BUT
    ##### CAN SERVE AS RECURSION PRACTICE, ALSO.


"""


##### FUNCTIONS WHERE RECURSION IS "NATURAL" ########


def print_nested_list(theinput):
    """Prints out every single string in theinput, one per line, UNLESS
    theinput is a string, in which case it just prints the input.

    Example:
    if theinput is
      [['this'], ['is', ['a', ['very', 'very', 'very'], ['nes ted', 'list']]]]
    then print_nested_list(theinput) should result in the following printout
       this
       is
       a
       very
       very
       very
       nes ted
       list

    Precondition: input is a string, or a potentially nested potentially empty
    list of strings."""
    if isinstance(theinput, str):
        print(theinput)
    if isinstance(theinput, list):
        for item in theinput:
            print_nested_list(item)

    # STUDENTS: implement this

    # Hint: since you want to do something different depending on whether
    # theinput is a list or a string, you'll want to use isinstance(theinput, list)
    # or not isinstance(theinput, list) or similarly for type string.

    # Note: there are several approaches that work, including using list
    # slicing, using a for-loop together with recursion, and using map.
    # (We may not cover `map` this semester.)


def embed(theinput):
    """Returns: depth of embedding, or nesting, in theinput.

    Examples:
        "the dog that barked" -> 0
        ["the", "dog", "that", "barked" ] -> 1
        ["the" ["dog", "that", "barked"]] -> 2
        ["the" ["dog", ["that", "barked"]] -> 3
        ["the" ["dog", ["that", ["barked"]] -> 4
        [[[["the"], "dog"], "that"], "barked"] -> 4

    Precondition: theinput is a string, or a potentially nested
    list of strings. No component list can be empty"""
    if isinstance(theinput, str):
         return 0

    if isinstance(theinput, list):
        count = 0
        for item in theinput:
            depth = embed(item)
            if depth > count:
                count = depth
        return 1 + count
     # Very compact solution given at
    # http://www.cs.cornell.edu/courses/cs1110/2014sp/lectures/lecture12/presentation-12.pdf


def max_nested_list(theinput):
    """Returns: The item with the largest value in theinput

    Example:
    sum_nested_list([0, [2, 5], 8, [-10, -1]]) should be  8

    Precondition: theinput is an integer, or a potentially nested
    non-empty list of integers. No component list can be empty"""
    # Base case: if the input is a list, we'll iterate through each item

    # Base case: if it's an int, that's the maximum we can return
    if isinstance(theinput, int):
        return theinput

    # Otherwise it's a non-empty list.  Compute the max of its first element:
    max_value = max_nested_list(theinput[0])

    # Now iterate over the rest of the list
    for item in theinput[1:]:
        # If item is a list, recurse; if it's an int, just use it directly
        if isinstance(item, list):
            candidate = max_nested_list(item)
        else:
            candidate = item
        # Keep the larger of candidate and current max_value
        if candidate > max_value:
            max_value = candidate

    return max_value

      # REPLACE WITH YOUR IMPLEMENTATION


def flatten_nested_list(theinput):
    """Returns: a COPY of theinput that is flattened.

    This function flattens every item in the theinput into a list with depth 1

    Example:
    flatten_nested_list(['this', ['is', 'a'], 'list', ['list', 'list' ]])
    should be ['this', 'is', 'a', 'list', 'list', 'list']

    Precondition: theinput a potentially nested non-empty list of strings.
    No component list can be empty"""
    results = []
    for item in theinput:
        if isinstance(item, list):
            results.extend(flatten_nested_list(item))
        else:
            results.append(item)
    return results
      # REPLACE WITH YOUR IMPLEMENTATION


##### FUNCTIONS WHERE FOR-LOOPS OR OTHER MECHANISM WOULD BE MORE "NATURAL", BUT
##### THERE IS AN INTERESTING RECURSION IDEA ALSO



def reverse1(thelist):
    """Returns: a COPY of thelist that is the reverse of the list.

        Example: the reverse of [1,2,3] is [3,2,1]

    Precondition: thelist is a list of ints"""
    if thelist == []:
        return []

    # Recursive case:
    #   reverse1(thelist[1:])  is the reverse of everything after the first element
    #   [thelist[0]]            is a single‑element list containing the first element
    # Concatenate them so that the first element ends up at the end.
    return reverse1(thelist[1:]) + [thelist[0]]
    # STUDENTS: implement this using recursion effectively
            # Do not use the method reverse().  That alters the list thelist.
            # Instead, implement this function with the following idea:
            # The reverse of thelist with at least one element is the
            # reverse of thelist[1:] concatenated with (a list with the element)
            # thelist[0].




def reverse2(thelist):
    """Returns: a COPY of thelist that is the reverse of the list.

        Example: the reverse of [1,2,3] is [3,2,1]

    Precondition: thelist is a list of ints"""
    if len(thelist)  <= 1:
        return thelist[:]

    return [thelist[-1]] + reverse2(thelist[1:-1]) + [thelist[0]]

    # STUDENTS: implement this using recursion effectively
            # Do not use the method reverse().  That alters the list thelist.
            # Instead, implement this function with the following idea:
            # To reverse a list thelist with at least two elements, switch
            # the first and last ones and reverse the middle.




##### FUNCTIONS WHERE FOR-LOOPS OR OTHER MECHANISM WOULD BE MORE "NATURAL", BUT
##### CAN SERVE AS RECURSION PRACTICE, ALSO.




def replace(thelist, a, b):
    """Returns: a COPY of thelist but with all occurrences of int a replaced by
    int b.  Does not change thelist.

        Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

    Precondition: thelist is a possibly empty list of ints."""
    # for item in range(len(thelist)):    # iterates by index
    #     if thelist[item] == a:
    #         thelist[item] = b       # for loop but changes/modify the list
    # return thelist

    # result = []           #for loop but creates a new copy
    # for val in thelist:           # iterates by item
    #     if val == a:
    #         result.append(b)
    #     else:
    #         result.append(val)
    # return result

    if not thelist:    #recursion
        return []
    first = thelist[0]
    if first == a:
        first = b
    return [first] + replace(thelist[1:], a, b)

     # STUDENTS: implement this using recursion effectively

def remove_first(thelist, v):
    """Returns: a COPY of thelist but with the FIRST occurrence of v
    removed (if present).

    Precondition: thelist is a list of ints
              v is an int"""
    # Base case: empty list 
    if not thelist:
        return []

    # If the first element is the one to remove, drop it and return the rest
    if thelist[0] == v:
        return thelist[1:]

    # Otherwise, keep the first element and recurse on the tail
    return [thelist[0]] + remove_first(thelist[1:], v)

      # STUDENTS: implement this using recursion effectively
