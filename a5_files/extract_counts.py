"""
Code for collecting word statistics for persuasive vs. unpersuasive
argument threads in CMV JSON.

Author: STUDENTS: Griffins Lelgut(gkl39)
    Stubs: Lillian Lee (LJL2)
Version: STUDENTS: 5th May, 2025
    Stubs: Apr 26, 2025
"""
from collections import Counter
import string

DEBUG_MODE = True  # If DEBUG_MODE: we use _Counter, a modified Counter class
                   # with a modified __str__() method.


# A subclass of Counter with __str__() modified for debugging purposes
class _Counter(Counter):
    # STUDENTS: update the class invariant to document instance attributes you
    # create
    """
    A substitute class for Counter.

    An instance collects counts just like a Counter does, but printing a _Counter
    yields a list of wordlists that have been used to create or update the object.
    """
    def __init__(self, wordlist=None):
        """
        Creates a new _Counter with its record of running text initialized
        to [wordlist]. Notice that this is a list that itself contains the list
        wordlist.

        If invoked by a call _Counter() with no argument, the running-text
        attribute should be initialized to the empty list.

        Precondition:
        wordlist: a list of strings
        """
        # STUDENTS: replace the line below with your implementation.

        if wordlist is None:
            super().__init__()
            self.running_text = []
        else:
            super().__init__(wordlist)
            self.running_text = [list(wordlist)]


    def update(self, other):
        """
        Updates the counts in `self` with the counts in `other`.

        If `other` is a _Counter, then the running text of `self` is updated by
        including the running text of `other`.

        Precondition: `other` is a Counter.
        """
        # STUDENTS:  Implement this method.

        super().update(other)
        if isinstance(other, _Counter):
            for wl in other.running_text:
                self.running_text.append(list(wl))

    def __str__(self):
        """
        Returns the str of this _Counter's running text list.
        """
        # STUDENTS: replace the line below with your implementation.
        # For the purposes of A5, do *not* call the superclass __str__

        return str(self.running_text)




if not DEBUG_MODE:
    _Counter = Counter  # redefine _Counter to be the regular Counter class.

# Helper
def canonicalize_text(s):
    """
    Returns a lowercased version of s with all punctuation replaced by a space.

    Punctuation is defined as any character in the string `string.punctuation`.

    Parameter s: a string

    Example: canonicalize_text('hi, HI, hi there!') -->  'hi  hi  hi there '
    """
    slist = list(s.lower())  # we can edit lists but not strings
    for idx in range(len(slist)):
        if slist[idx] in string.punctuation:
            slist[idx] = ' '
    return ''.join(slist)


# Main function
def extract_counts(comment_node):
    """Returns a dictionary with a Counter of either the words in delta-paths in
    comment_node's conversation tree or, if there is no delta, all the words in
    the tree.

    Key "has_delta" in the returned dictionary: True if DeltaBot has authored
    any text in the conversation tree, False otherwise.

    Key "word_counts": Counter.

        * If the value for key "has_delta" is True, "word_counts" is for just the
          words in replies in paths leading to a DeltaBot-authored post
          (possibly including comment_node itself).

        * If the value for key "has_delta" is False, "word_counts" counts
          the words for all replies in the conversation tree.

    This function lower-cases and splits text on punctuation and whitespace
    before processing its words.

    Precondition:
    comment_node: a dictionary in some list of children in a valid conversation
    tree.
    """
    # Note: The specification doesn't mention the private class _Counter, because
    # it's, well, meant to be private.

    assert isinstance(comment_node, dict), f"extract_counts: input is not a dict but a {type(comment_node)}"
    assert 'data' in comment_node, f"extract_counts: cannot find key 'data'"

    # Special case: truncated path
    # We should probably throw out the entire comment node, but are ignoring
    # this issue for simplicity in A5.
    if comment_node["kind"] == "more":
        return {"has_delta": False, "word_counts": _Counter()}

    data = comment_node['data']  # Useful abbreviation

    # Store the text of the comment node itself, since it will always be part of
    # the text used for this comment node
    word_counts_val = _Counter(canonicalize_text(data["body"]).split())

    # Keep track of whether we've found a delta so far
    found_delta = (data["author"] == "DeltaBot")

    # Base case: no replies
    if data["replies"] == "":
        return {"has_delta": found_delta,
                "word_counts": word_counts_val}

    # Recursive case: at least one reply
    # Set up some helpful variables
    children = data["replies"]["data"]["children"]  # list
    delta_children_results = _Counter()  # accumulator
    non_delta_children_results = _Counter()  # accumulator, only useful if
                                             # no deltas are found.

    for child in children:
        child_results = extract_counts(child)
        if child_results["has_delta"]:
            found_delta = True
            delta_children_results.update(child_results["word_counts"])
        elif not found_delta:
            # If we found a delta, we won't use non-delta children
            non_delta_children_results.update(child_results["word_counts"])

    # Now combine recursive results
    if found_delta:
        # We want to combine text just for delta paths.
        word_counts_val.update(delta_children_results)
    else:
        # This should be all the results
        word_counts_val.update(non_delta_children_results)

    return {"has_delta": found_delta,
            "word_counts": word_counts_val}


def per_and_unper_counts(comment_tree):
    """
    Returns a dictionary of two word-count dictionaries:

    Key "per_counts" is for the persuasive texts in comment_tree
    Key "nonper_counts" is for the nonpersuasive texts in comment_tree.

    Preconditions:
    comment_tree: Reddit conversation tree loaded from JSON
    """
    # We use extract_counts() as a helper in our implementation

    top_level_children = comment_tree[1]["data"]["children"]

    # Word counts so far for our two types of text
    per_counts = _Counter()
    nonper_counts = _Counter()

    for child in top_level_children:
        child_data = extract_counts(child)

        # Decide which Counter to add the child's data to
        if child_data["has_delta"]:
            storage = per_counts
        else:
            storage = nonper_counts

        storage.update(child_data["word_counts"])

    return {"per_counts": per_counts, "nonper_counts": nonper_counts}


def compare_usage(target_words, per_counts, nonper_counts):
    """Computes the percentage of target words in the persuasive texts and
    the nonpersuasive texts.

    Returns a dictionary:
        * Key "persuasive rate": sum of the target words' counts in per_count
            divided by the sum of all counts in per_count.
        * Key "nonpersuasive rate": ditto, but for nonper_counts

    Preconditions:
    target_words: non-empty list of strings, each representing a word
    per_counts: a Counter
    nonper_counts: a Counter
    """
    # counts so far for any word in target_words
    sum_per = 0
    sum_nonper = 0
    for target_word in target_words:
        sum_per += per_counts[target_word]
        sum_nonper += nonper_counts[target_word]

    # We will let callers decide what to do if a division-by-zero error occurs
    return {"persuasive rate": sum_per/per_counts.total(),
            "nonpersuasive rate": sum_nonper/nonper_counts.total()}
