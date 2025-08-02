"""
Functions involving nested lists.

These functions all require for-loops.

Initial skeleton by W. White (wmw2), cuts and minor edits by Lillian Lee (LJL2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only
    numbers in it.

    Example: row_sums([[0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]])
    returns [0.9, 1.5, 1.7]

    Example: row_sums([[0.2, 0.1], [-0.2, 0.1], [0.2, -0.1], [-0.2, -0.1]])
    returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with no header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) each row contains
    only numbers, and (3) each row is the same length.
    """
    sums = []
    for lst in table:
        list_sum = 0
        for item in lst:
            list_sum += item
        sums.append(list_sum)
    return sums
      # STUDENTS: implement using nested for-loops.



def place_sums(table):
    """
    Modifies table to add a column of row sums.

    This function assumes that table has a header, which means the first row
    only has strings in it.  The later rows are only numbers.  This function
    adds the string 'Sum' to the first row.  For each later row, it appends
    the sum of that row.


    Example: Suppose that `a` is

        [['First', 'Second', 'Third'],
         [0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]]

    then place_sums(a) modifies the table a so that it is now

         [['First', 'Second', 'Third', 'Sum'],
          [0.1, 0.3, 0.5, 0.9], [0.6, 0.2, 0.7, 1.5], [0.5, 1.1, 0.1, 1.7]]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with a header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) the first row only
    contains strings (the headers) (3) each row after the first contains only
    numbers, and (4) each row is the same length.
    """

    table[0].append('Sum')
    for row in range(1, len(table)):
        row_sum = 0
        for column in range(len(table[row])):
            row_sum += table[row][column]

        table[row].append(row_sum)


    # STUDENTS: implement using nested for-loops.


### OPTIONAL EXERCISES ###
def crossout(table,row,col):
    """
    Returns a copy of the table, missing the given row and column.

    Example: crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
    Example: crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
    Example: crossout([[1,3],[6,2]],0,0) returns [[2]]
    Example: crossout([[6]],0,0) returns []

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.

    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table

    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    new_table = []

    for i in range(len(table)):
        if i == row:
            continue

        new_row = []
        for j in range(len(table[i])):
            if j == col:
                continue
            new_row.append(table[i][j])
        new_table.append(new_row)

    return new_table


      # STUDENTS: implement using for-loops. Consider looping over indices.
