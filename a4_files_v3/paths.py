"""
Functions for finding interesting paths in Reddit CMV conversation trees.

Reddit conversation-tree JSON is described (as "comment trees") in
https://github.com/Pyprohly/reddit-api-doc-notes/blob/main/docs/api-reference/comment_tree.rst

Author: STUDENTS: Griffins Lelgut (gkl39), Geu Kuei (ga362)
    Stubs: Lillian Lee (LJL2), with some text for the specification of
    path_to_delta() contributed by Michael Clarkson (MRC26)
Version: STUDENTS: Apr 14, 2025
    Stubs: Mar 27, 2025 (documentation updated Apr 2, 2025)
"""
def longest_thread(comment_node):
    """Return a list of the bodies of the comments in the longest thread starting
    from comment_node.

    Ties may be broken arbitrarily.

    The list should be in order of "topmost" comment first.

    The list contains just the text (body) of comment_node if comment_node's data's
    replies is the empty string (meaning no replies).

    The list contains just the string "**truncated**" if the value for key "kind"
    of this comment_node is "more", and we treat the thread as if it had length 1.

    :param dict comment_node: a dictionary in some list of children in the
    comments dictionary for a valid conversation tree.

    For the bench-clearing tree of t3_2rpvc7, the names of the possible
    comment_nodes and schematic of the desired output are as follows.

    t1_cnibo8i --> [body of t1_cnibo8i, body of t1_cnikfa7]
    t1_cnikfa7 --> [body of t1_cnikfa7]
    t1_cni6vol --> [body of t1_cni6vol, body of t1_cni7f98, body of t1_cniszwq, body of t1_cnjaebu]
    t1_cni7f98 --> [body of t1_cni7f98, body of t1_cniszwq, body of t1_cnjaebu]
    t1_cniszwq --> [body of t1_cniszwq, body of t1_cnjaebu]
    t1_cnjaebu --> [body of t1_cnjaebu]
    t1_cni5tm6 --> [body of t1_cni5tm6]
    """
    # STUDENTS: leave these safeguard asserts in.
    # They halt execution with an error message if the boolean expressions are false
    assert isinstance(comment_node, dict), f"longest_thread: input is not a dict but a {type(comment_node)}"
    assert 'data' in comment_node, f"longest_thread: cannot find key 'data'"

    if comment_node.get('kind') == 'more':
        return ["**truncated**"]

    data = comment_node['data']
    if not data.get('replies'):
        return [data.get('body', '')]

    children = data['replies']
    if isinstance(children, str) or 'data' not in children:
        return [data.get('body', '')]

    max_thread = []
    for child in children['data']['children']:
        thread = longest_thread(child)
        if len(thread) > len(max_thread):
            max_thread = thread

    return [data.get('body', '')] + max_thread
     # STUDENTS: your implementation must be fundamentally based on recursion
          # with the restrictions described in the handout.
          # You are not allowed to use the value of the key `depth`.
          # See handout Section 4.4 for more on the "truncated" case



def path_to_delta(comment_node):
    """
    Finds a thread starting at comment_node and containing a post by DeltaBot.
    Returns a list of the text bodies of the comments in that thread,
    starting with the body of comment_node and ending with and including the
    body of the DeltaBot post; does not include any posts in the thread that
    might be below the DeltaBot post. If there is no such thread, returns the
    empty list. If there are multiple such threads, chooses one of them
    arbitrarily.

    The returned list is empty if the value for key "kind" of this comment_node
    is "more", and we treat this truncated thread as if it had no deltas awarded.

    :param dict comment_node: a dictionary in some list of children in the
    comments dictionary for a valid conversation tree.

    Example: for file '3mzc6u_tontine.json', there is a path to a delta from
    comment with name t1_cvjf7y0, but not from any of the other top-level
    comments.

    """
    # STUDENTS: leave these safeguard asserts in.
    # They halt execution with an error message if the boolean expressions are false
    assert isinstance(comment_node, dict), f"longest_thread: input is not a dict but a {type(comment_node)}"
    assert 'data' in comment_node, f"longest_thread: cannot find key 'data'"

    if comment_node.get('kind') == 'more':
        return []

    data = comment_node['data']
    author = data.get('author', '')
    body = data.get('body', '')

    if author == 'DeltaBot':
        return [body]

    if not data.get('replies'):
        return []

    replies = data['replies']
    if isinstance(replies, str) or 'data' not in replies:
        return []

    for child in replies['data']['children']:
        subpath = path_to_delta(child)
        if subpath:
            return [body] + subpath

    return []
          # STUDENTS:
          # 1. Your implementation must be fundamentally based on recursion
          #    with the restrictions described in the handout.
          # 2. You are not allowed to create a string equivalent of comment_node
          #   and search through that.
          # 3. See handout Section 4.4 for more on the "truncated" case.
          # 4. To see if the author was DeltaBot, look for the key "author"
