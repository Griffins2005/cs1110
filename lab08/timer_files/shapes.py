"""
Module containing two classes: Point3 and Rectangle.

Author: Walker M. White (wmw2), Anne Bracy (awb93), Lillian Lee (LJL2),
        Daisy Fan (kdf4), Michael Clarkson (mrc26)
Version: 2/17/25
"""

import math


class Point3():
    """
    An instance is a point in 3D space.

    Attributes:
    x: the x coordinate of the point
    y: the y coordinate of the point
    z: the z coordinate of the point

    Constructor function:
    Point3(x, y, z) creates an instance with the given coordinates.
    Example: shapes.Point3(4, 6, 5) is a point with x coordinate 4,
      y coordinate 6, and z coordinate 5.
    """

    def __init__(self, x, y, z):
        """
        Creates a new Point with the given coordinates, each is a number.
        """
        self.x = x
        self.y = y
        self.z = z


    def distance(self, other):
        """
        Returns the Euclidean distance between self and other.

        other: an instance of Point3
        """
        return math.sqrt(  (self.x - other.x) ** 2
                         + (self.y - other.y) ** 2
                         + (self.z - other.z) ** 2 )


class Rectangle():
    """
    An instance is a rectangle in 2D space.

    Attributes:
    left and bottom: numbers that together are the coordinate of the
      lower-left corner of the rectangle.
    right and top: numbers that together are the coordinate of the
      upper-right corner of the rectangle.

    Constructor function:
    Rectangle(l, b, r, t) creates a rectangle with the lower-left
      corner at (l, b) and the upper-right corner at (r, t)
    Example: shapes.Rectangle(3, 4, 7, 5) is a rectangle with
      corners (3,4) and (7,5).
    """

    def __init__(self, left, bottom, right, top):
        """
        Creates a new Rectangle with the given coordinates.

        Preconditions: left, bottom, right, top are each a number and
        left<right and bottom<top

        """
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


    def area(self):
        """
        Returns the area of the rectangle.
        """
        width = self.right - self.left
        height = self.top - self.bottom
        return width * height
