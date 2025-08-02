"""
Convenience functions for processing JSON Reddit conversation-tree data.

Reddit conversation-tree JSON is described (as "comment trees") in
https://github.com/Pyprohly/reddit-api-doc-notes/blob/main/docs/api-reference/comment_tree.rst.

Author: STUDENTS: Griffins Lelgut (gkl39), Geu Kuei (ga362)
    Stubs: Lillian Lee (LJL2), with some of specification text for backbone()
    contributed by Michael Clarkson (MRC26)
Version: STUDENTS: Apr 14, 2025
    Stubs: Apr 2, 2025
"""

import json  # Python package for managing JSON data


def json_to_pretty(some_json):
    """
    Return a string version of some_json with visual indentation for its structure ("pretty-print" it).

    Dictionary keys will be sorted alphabetically.

    some_json: valid JSON
    """
    return json.dumps(some_json,sort_keys=True,indent=2,separators=(',', ': '))


def check_json(conv_tree):
    """Stop execution with an AssertionError if conv_tree doesn't seem like
    a valid conversation tree

    :param list conv_tree: Reddit conversation tree loaded from JSON

    """
    # Quits with an AssertionError if the boolean expression is False, printing
    # the specified error string
    assert isinstance(conv_tree, list),  \
        f"check_json: wrong arg type {type(conv_tree)}"
    assert len(conv_tree) == 2, f"check_json: wrong arg length {len(conv_tree)}"
    assert conv_tree[0]["kind"] == 'Listing', "check_json: unexpected content"
    assert conv_tree[1]["kind"] == 'Listing', "check_json: unexpected content"


def backbone(pretty_json_conv_tree, char_cutoff):
    """
    Return a string giving an overview of the structure of pretty_json_conv_tree.

    The returned string is comprised of every line in pretty_json_conv_tree
    that starts with any amount of whitespace followed by any of the following
    strings (excluding the enclosing single quotes).
        '"name":'
        '"selftext":'
        '"author":'
        '"parent_id":'
        '"body":'
    Further, each line in the returned string is abridged: the first 12
    characters (which will be just whitespace) of the original line are
    omitted, and after that as many characters as possible are included
    up to a limit `char_cutoff`.
    The returned lines are ordered as they were in pretty_json_conv_tree.
    A single newline ('\n') character separates each of the returned lines.

    The very first set of three such lines represents the original post, and
    is followed by a "divider bar" consisting of `char_cutoff` hyphens in the
    returned string.

    :param str pretty_json_conv_tree: Reddit conversation-tree JSON that has
     been passed through json_to_pretty.

    :param int char_cutoff:  how many characters to include for each line

    Example for char_cutoff 80, JSON for CMV submission 2rpvc7:

    The actual return string:
    '"author": "The_Aesir9613",\n"name": "t3_2rpvc7",\n"selftext": "\\n\\n_____\\nIt\'s my opinion that bench clearings in baseball hurts t\n--------------------------------------------------------------------------------\n"author": "Kman17",\n"body": "I\'d be a little bit cautious of removing the self-policing elements out\n"name": "t1_cnibo8i",\n"parent_id": "t3_2rpvc7",\n          "author": "The_Aesir9613",\n          "body": "Good points.  I would argue though that Hockey fights aren\'t \n          "name": "t1_cnikfa7",\n          "parent_id": "t1_cnibo8i",\n"author": "CherrySlurpee",\n"body": "They really actually help the sport.\\n\\nBaseball, to most people, is a \n"name": "t1_cni6vol",\n"parent_id": "t3_2rpvc7",\n          "author": "The_Aesir9613",\n          "body": "They can be exciting, yes, but that only means people enjoyed\n          "name": "t1_cni7f98",\n          "parent_id": "t1_cni6vol",\n                    "author": "SOLUNAR",\n                    "body": "&gt; That doesn\'t mean they enjoyed watching baseba\n                    "name": "t1_cniszwq",\n                    "parent_id": "t1_cni7f98",\n                              "author": "The_Aesir9613",\n                              "body": "It\'s not a legitimate argument to say bas\n                              "name": "t1_cnjaebu",\n                              "parent_id": "t1_cniszwq",\n"author": "MageZero",\n"body": " Major League Baseball has not only survived, but flourished for 145 ye\n"name": "t1_cni5tm6",\n"parent_id": "t3_2rpvc7",'

    How that string looks when printed:
"author": "The_Aesir9613",
"name": "t3_2rpvc7",
"selftext": "\n\n_____\nIt's my opinion that bench clearings in baseball hurts t
--------------------------------------------------------------------------------
"author": "Kman17",
"body": "I'd be a little bit cautious of removing the self-policing elements out
"name": "t1_cnibo8i",
"parent_id": "t3_2rpvc7",
          "author": "The_Aesir9613",
          "body": "Good points.  I would argue though that Hockey fights aren't
          "name": "t1_cnikfa7",
          "parent_id": "t1_cnibo8i",
"author": "CherrySlurpee",
"body": "They really actually help the sport.\n\nBaseball, to most people, is a
"name": "t1_cni6vol",
"parent_id": "t3_2rpvc7",
          "author": "The_Aesir9613",
          "body": "They can be exciting, yes, but that only means people enjoyed
          "name": "t1_cni7f98",
          "parent_id": "t1_cni6vol",
                    "author": "SOLUNAR",
                    "body": "&gt; That doesn't mean they enjoyed watching baseba
                    "name": "t1_cniszwq",
                    "parent_id": "t1_cni7f98",
                              "author": "The_Aesir9613",
                              "body": "It's not a legitimate argument to say bas
                              "name": "t1_cnjaebu",
                              "parent_id": "t1_cniszwq",
"author": "MageZero",
"body": " Major League Baseball has not only survived, but flourished for 145 ye
"name": "t1_cni5tm6",
"parent_id": "t3_2rpvc7",
    """

    # Stop execution if given unexpected argument type, printing the
    # given error message.
    assert isinstance(pretty_json_conv_tree, str), \
        f"backbone: wrong arg type {type(pretty_json_conv_tree)}"

    # STUDENTS: keep the `jlines=...` line in.
    # It is a list of the lines in pretty_json_conv_tree.
    # You may want to temporarily print its first few lines to see what it
    # looks like; but remove those print statements before submitting.
    jlines = pretty_json_conv_tree.split('\n')

    result_lines = []
    keys_to_keep = ['"name":', '"selftext":', '"author":', '"parent_id":', '"body":']
    post_lines_count = 0

    for line in jlines:
        stripped = line.lstrip()
        matched_key = None

        for key in keys_to_keep:
            if stripped.startswith(key) and matched_key is None:
                matched_key = key
                trimmed_line = line[12:][:char_cutoff]
                result_lines.append(trimmed_line)
                post_lines_count += 1

        if matched_key and post_lines_count == 3:
            result_lines.append('-' * char_cutoff)
            post_lines_count += 1

    return '\n'.join(result_lines)


    # STUDENTS: When implementing this function:
    # 1. Don't use recursion if it isn't necessary. Instead, consider
    #    using a for-loop on `jlines`, initialized above.
    # 2. You'll eventually want to return a string, but we recommend
    #    having a list accumulate the necessary strings, and then use
    #    '\n'.join() at the very end.  This handles the separation by newlines
    #    and more efficient than concatenating strings within a loop.
    # 3. You don't have to handle the indentation except for omitting the first
    #    12 characters: After the first 12 spaces, the fact that the input is
    #    already pretty-printed means the lines in `jlines` have the correct
    #    amount of whitespace at the line start already.
    # 4. See the "bar chart" printing example from lecture for inspiration on
    #    how to create the divider bar.
