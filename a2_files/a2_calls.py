""" Functions and calls involving Users and Posts 

Author: Lillian Lee (LJL2)
Version: Feb 24, 2025
"""

from a2_classes import User, Post

def incr(obj): 
    """
    If obj is a User, adds 1 to the User's num_posts and returns True
    If obj is a Post, adds 1 to the Post's num_share and returns True
    Otherwise, does nothing but return False

    obj: is not None
    """
    if isinstance(obj, User):
        obj.num_posts = obj.num_posts + 1
        return True
    elif isinstance(obj, Post):
        obj.num_shares = obj.num_shares + 1
        return True
    else:
        return False


def post_new(author, content):
    """
    Returns a new Post by `author` with text `content`.

    It doesn't matter if there's a Post with the exact same content.

    author: a User (cannot be None)
    content: a non-empty string.
    """ 
    return Post(content, author, None)


def post_share(new_author, orig):
    """
    Returns a new Post by new_author with text content taken from orig.

    The num_posts of new_author is incremented.
    The num_shares of orig is incremented. 
    The share_of of new Post is orig. 

    new_author is a User (cannot be None)
    orig is a Post (cannot be None).  
    """
    if orig.share_of is None:
        np = post_new(new_author, orig.text)
        np.share_of = orig
        incr(orig)
    else:
        np = post_share2(new_author, orig.share_of)

    return np


def post_share2(new_author, orig):
    """
    Same specification as post_share's (omitted to reduce line count)
    """
    if orig.share_of is None:
        np = post_new(new_author, orig.text)
        np.share_of = orig
        incr(orig)
    else:
        np = post_share2(new_author, orig.share_of)

    return np


cornell = User("CornellU")
fan = User("GoBigRed")
fanfan = User("echo")

p = post_new(cornell, "News")
announce1 = post_new(cornell, "We're #1 again!")
reshare = post_share(fan, announce1)
tempx = post_share(fanfan, reshare)
