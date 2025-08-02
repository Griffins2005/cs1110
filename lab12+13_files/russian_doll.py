"""
Module containing one class: Doll

Author: Anne Bracy (awb93), Lillian Lee (LJL2)
Date:   Mar 13, 2019; Apr 2 2021
"""

class Doll():
    """
    An instance is a nesting Doll (matryoshka).
    
    attributes:
        name: a nonempty string
        innerDoll: another Doll, or None
        hasSeam: True if innerDoll is not None, False otherwise.

    Class invariant: no Doll can contain itself (either directly or indirectly).
        Users are responsible for maintaining the correspondence between 
        innerDoll's value and hasSeam's value.

    Constructor call to create an empty Doll with name 'A' and 
    attribute hasSeam False:
        Doll('A')
    If d1 is an existing Doll, here is a constructor call to
    create a Doll with with name 'B', innerDoll d1, and hasSeam attribute set to True:
        Doll('B', d1).

    """
    
    def __init__(self, name, innerDoll):
        """
        Creates a new Doll with a name and an inner Doll
        """
        self.name = name
        self.innerDoll = innerDoll
        if innerDoll == None:
            self.hasSeam = False
        else:
            self.hasSeam = True

    def __eq__(self, other):
        if not isinstance(other, Doll):
            return False
        elif not self.name == other.name and self.hasSeam == other.hasSeam:
            return False
        else:
            return self.innerDoll == other.innerDoll

    def __str__(self):
        out =  "'" + self.name + "'" + ". Inner doll: "
        if self.innerDoll is None:
            out += "None"
        else:
            out += self.innerDoll.__str__() 
        return out




