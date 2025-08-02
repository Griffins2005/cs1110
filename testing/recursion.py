class Person:
    """ Objects represent an individual with a name, birth year, 
        and a list of known parents

    Attributes:
        name [str]: name of pereson 
        birthyear [int]: year the person was born
           must be > 0 (there is no BC)
           must be < 2023
        parents [list of persons]: list of persons, possibly empty

    You may assume everyone is born later than their parents.
    You may assume no person appears twice in a family tree.  """

    def __init__(self, n, y, rents):
        """ Creates a new person with a name and parents """
        self.name = n;
        self.birthyear = y;
        self.parents = rents

def find_waldo_broken(p):
    """  Returns: 
             True  if any ancestor of p (including p) has the name "Waldo"
             False if no ancestor of p (including p) has the name "Waldo"
         Precondition (no need to assert): p is a person                  
    """
    if p.name == "Waldo":
        return True
    found = False
    for parent in p.parents:
        found = find_waldo_broken(parent)
    return found

def find_waldo(p):
    """  Returns: 
             True  if any ancestor of p (including p) has the name "Waldo"
             False if no ancestor of p (including p) has the name "Waldo"
         Precondition (no need to assert): p is a person               """
    if p.name == "Waldo":
        return True
    for parent in p.parents:
        if find_waldo(parent):
            return True
    return False

def earliest_bruno(p):
    """
    Returns: the birthyear of the earliest born ancestor named "Bruno"
             None if there is no ancestor named "Bruno"
             this includes p

    Example:  if there are two ancestors named "Bruno" born in 2000 and 1909,
                     --> returns 1909

    Precondition (no need to assert): p is a person                 """

if __name__ == '__main__':

    t1 = Person("Tito", 1975, [])
    t2 = Person("Timmy", 1960, [])
    t3 = Person("Tina", 1950, [])
    t4 = Person("Timo", 2000, [])

    b1 = Person("Bruno", 1500, [])
    b2 = Person("Bruno", 1600, [b1,t1])
    b3 = Person("Bruno", 1700, [])
    b4 = Person("Bruno", 1800, [b2,b3,t2])
    b5 = Person("Bruno", 1900, [b4,t4])

    t5 = Person("Timo", 2010, [b3,t3])
    
    testcases = [[b1, 1500],
                 [t1, None],
                 [b2, 1500],
                 [b5, 1500],
                 [b3, 1700],
                 [b4, 1500],
                 [t5, 1700]
                 ]

    for item in testcases:
        p = item[0]
        expected = item[1]

        result = earliest_bruno(p)
        print(p.name + ": "+str(result)) 
        assert result == expected, \
        "Bad result on person " + p.name + ": " + str(result)
    print("Tests ran without crashing")

