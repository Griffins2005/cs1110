"""

Classes for modeling social-media users and posts

Author:  Lillian Lee (LJL2)
Version: Feb 23, 2025
"""


class User:
    """A User is a user on the social media site.

    Attributes:
    handle [non-empty str]: the handle, aka username, of the User
    num_posts [non-negative int]: the number of posts authored by this User

    Constructor function:
    User(h) creates a User with handle h, and num_posts set to 0.
    """

    def __init__(self, h):
        """ Creates a new User with handle h and num_posts set to 0"""
        self.handle = h
        self.num_posts = 0

    def __str__(self):
        """ Returns string of form
            User <handle>, num_posts: <num_posts>
        """
        return 'User '+self.handle+", num_posts: "+str(self.num_posts)


class Post:
    """ A Post can be a new social-media post or a reshare of an existing one.

    Attributes:
    text [non-empty str]: the text of the Post
    author [User, cannot be None]: the User who created this Post.
        If this Post is a reshare, the author is the person who reshared, not
        the author of the original Post.
    num_shares [non-negative int]: number of times this Post has been shared
    share_of [Post or None]: 
        If this Post is a reshare, share_of is the original Post.
        Otherwise, share_of is None.

    Constructor function:
    Post(t, a, so) creates a Post with text t, author a, num_shares of 0, and
      share_of value so. It *also* adds 1 to the num_posts of author a.
    """

    def __init__(self, t, a, so):
        """
        Creates a new Post with text t, author a,  num_shares of 0, and
        share_of value so.

        The num_posts of author `a` is incremented.

        t: non-empty str
        a: User object, cannot be None
        so: either a Post object or None.
        """
        self.text = t
        self.author = a
        a.num_posts = a.num_posts + 1
        self.num_shares = 0
        self.share_of = so

    def __str__(self):
        """ Returns string of form
                Post by <handle>, share count: <num_shares>, is a reshare, text is
                  <text>
            where a "not" is inserted if this is a reshare.

        """
        out = 'Post by '+self.author.handle+", share count: "+str(self.num_shares)
        if self.share_of is  None:
            out = out + ", is not a reshare"
        else:
            out = out + ", is a reshare"
        out = out + ", text is\n  "+self.text
        return out