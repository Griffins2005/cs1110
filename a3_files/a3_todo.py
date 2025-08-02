"""
Functions for maintaining a schedule of tasks.

# STUDENTS: fill in Author, Source consulted, and Version
Author:
    Skeleton: William Xiao (wmx2) and Lillian Lee (LJL2)
    w/ input from Rhea Bansal (rab378), Kevin Cook (kjc244)
    Group: Griffins K. Lelgut (gkl39), Michael Sanchez (ms3627)
Sources consulted: None
Version: A3
    Skeleton last update Sat Mar 8 2025
"""


# STUDENTS: this function can be useful for debugging
def sirialize(day):
    """
    Prints out the tasks scheduled in Day `day` in chronological order.

    Parameter day: the Day whose data should be printed out.
    Precondition: day is a Day object.
    """
    print(day.name + ":")

    # collect the unique events / tasks in the day, with their start time
    tasks_already_collected = []
    found = False  # whether we found any tasks
    for time in range(len(day.time_slots)):
        task = day.time_slots[time]
        if task is not None and task not in tasks_already_collected:
            found = True
            tasks_already_collected.append(task)
            print(str(time)+":00-"+str(time+task.length)+":00 "+task.name)
    if not found:
        print("No events scheduled.")


def space_available(day, task, start):
    """
    Returns: True if `task` could be scheduled on `day` at `start`,
    False otherwise.

    `task` can be scheduled if there's a continuous run of empty timeslots in
    `day`'s time_slots that:
        * starts at `start`, and
        * is at least as long as the length of `task`.

    day: a Day.
    task: a Task.
    start: an int, 0 <= start < 24

    """
    if start + task.length > 24:
        return False

    for hour in range(start, start + task.length):
        if hour >= 24 or day.time_slots[hour] is not None:
            return False

    return True



def add_task(day, task, start_time):
    """
    Returns: True if Task `task` is added to Day `day` at time `start_time`
    successfully, False otherwise.

    If `task` can be scheduled, two things happen:
    * the `time_slots` attribute of `day` is modified so that the requisite
    number of elements (i.e., as many as `task` is long, measured in hours)
    in `time_slots` starting at position `start_time` are all set to `task`.
    * 1 is added to the num_tasks_scheduled of `day`.

    `task` cannot be added to `day` if there's another Task occupying any of
    the necessary hours. For example, adding a 3-hour Task at 2:00 should fail
    if there are any Tasks scheduled between the hours of 2:00 (inclusive) and
    5:00 (exclusive).

    Also, `task` also cannot be added if scheduling it at the given
    time would require rolling over to the next day to finish. As an example,
    trying to schedule a 2-hour task should fail if start_time is 23.

    If the given task cannot be added, neither `day` nor `task` should be changed.

    Parameters:
    day: a Day object.
    task: a Task object.
    start_time (int): 0 <= start_time < 24.
    """

    if space_available(day, task, start_time):

        for hour in range(start_time, start_time + task.length):
            day.time_slots[hour] = task
        day.num_tasks_scheduled += 1
        return True
    else:
        return False


def propose_mtg_times(cal1, cal2, task):
    """
    Returns a chronologically-sorted list of times for which `task` could be
    scheduled on both cal1 and cal2, where these represent two different
    people's calendars for the same day.

    The returned list has items of the form "<start hour>:00-<end hour>:00" in
    24-hour time, e.g, "9:00-13:00".  It may be empty.

    Parameters:
    cal1, cal2: two different Day objects (although the availabilities could be
    exactly the same.)
    task: a Task

    """

    available_times = []

    for start in range(24):
        if space_available(cal1, task, start) and space_available(cal2, task, start):
            end = start + task.length
            time_slot = str(start) + ":00-" + str(end) + ":00"
            available_times.append(time_slot)

    return available_times
