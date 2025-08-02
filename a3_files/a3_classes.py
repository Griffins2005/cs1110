"""
Provides classes Task and Day for scheduling tasks.

Author: Kevin Cook  (kjc244), w/ input from Rhea Bansal (rab378),
Lillian Lee (ljl2), William Xiao (wmx2)
Version: Sun Mar 2 2025
"""


class Task:
    """
    An instance is a task that takes at most 24 hours to complete.

    Attributes:
    name (nonempty string): the name of this Task
    length (int in 1, 2, ..., 24): how long this Task takes to complete, in hours

    It is allowed for different Tasks to have the same name and length.

    Constructor function:
    Task(n, i) creates a Task with name n and length i.
    """
    def __init__(self, name, length):
        """
        Initializer: a new Task with the given name and length

        Preconditions:
        name: nonempty string
        length: an int in 1, 2, ..., 24, inclusive
        """
        self.name = name
        self.length = length


class Day:
    """
    An instance is a 24-hour day. Tasks can be scheduled on the hour.

    Attributes:
    name (nonempty string): the name of this day. Example: "Monday"
    time_slots (length-24 list, each element either a Task or None):
        the time slots that make up this day.
    num_tasks_scheduled (non-negative int): the number of Tasks that have
        been scheduled for this Day.

    Multiple time slots can contain the same Task, since a Task can take more
    than one hour to complete.

    Constructor function:
    Day(n) creates a Day with name n, all entries in time_slots set to None,
    and num_tasks_scheduled set to 0.
    """
    def __init__(self, name):
        """
        Initializer: a new Day with name `name`, all time_slots entries None,
        0 num_tasks_scheduled.

        name: nonempty string
        """
        self.name = name
        self.time_slots = []
        for i in range(24):
            self.time_slots.append(None)
        self.num_tasks_scheduled = 0


