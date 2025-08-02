"""
Tests for a3_todo

# STUDENTS: fill in Author, Source consulted, and Version

Author:
    Skeleton: Lillian Lee (LJL2), William Xiao (WMX2)
Sources consulted:
Version:
    Skeleton released Sun Mar 2 2025
"""

import a3_classes
import a3_todo
import cornellasserts


# globals setting things up somewhat like assignment diagram
predef1 = a3_classes.Task("SPCA shift", 3)
predef2 = a3_classes.Task("work-study", 2)
predef3 = a3_classes.Task("cure cancer", 3)
predef4 = a3_classes.Task("Study for prelims", 4)
predef5 = a3_classes.Task("Conquer enemies", 24)
todo_call = a3_classes.Task("Call mom", 1)
todo_hack = a3_classes.Task("Programming sprint", 6)
DAY_POOL = [a3_classes.Day("Monday March 2"),  # all time_slots are None
            a3_classes.Day("Monday March 9"),  # all time_slots are None
            a3_classes.Day("Ides of March"),   # all time_slots are None
            a3_classes.Day("Monday March 16")  # all time_slots are None
            ]




# Helper for checking against accidental changes in tasks
def assert_task_unchanged(task, name, length):
    """Quits with error if task.name != name or task.length != length."""
    if task.name != name or task.length != length:
        msg = "Task has unexpected attribute."
        msg += " Its name is " + task.name
        msg += " and its length is " + str(task.length)
        cornellasserts.quit_with_error(msg)


def test_space_available():
    """Test space_available."""
    print("Running test_space_available")

    # STUDENTS: Comment and fix any incorrect ones we have planted; follow
    # the conventions of Assignment.
    # You must also complete test case #3 as instructed.

    # Empty Day tests
    # First, create a Day
    d = a3_classes.Day("NYE")

    # 1. space available for a Task of length of 1
    task = a3_classes.Task("test", 1)
    for h in range(24):
        cornellasserts.assert_equals(True, a3_todo.space_available(d, task, h))

    # 2. space available for a Task running multiple hours, unless hours run out
    task = a3_classes.Task("test", 3)
    for h in range(22):
        cornellasserts.assert_equals(True, a3_todo.space_available(d, task, h))
    for h in range(22,24):  #changed 21 to 22
        cornellasserts.assert_equals(False, a3_todo.space_available(d, task, h))

    # 3. space available for a 24-hour Task, but only if it starts at hour 0
    task.length = 24
    cornellasserts.assert_equals(True, a3_todo.space_available(d, task, 0))
    for h in range(1, 24):
        cornellasserts.assert_equals(False, a3_todo.space_available(d, task, h))

    # STUDENTS: use a for-loop over a range() (NOT a list)
    # to run a assert_equals() test that for every hour other than 0,
    # space_available returns False.
    # Take a look at at test case 12 for an example.

    # Tests for a Day that already has an Task on it.
    # First, add a single Task `added` that takes multiple hours
    # We can't yet use a3_todo.add_task because we don't know if it's correct.
    added = a3_classes.Task("added, 8-11am", 3)
    for h in [8,9,10]:
        d.time_slots[h] = added
        d.num_tasks_scheduled = d.num_tasks_scheduled + 1

    # 4. space available before and after `added` for a short Task
    task = a3_classes.Task("test", 2)
    for h in list(range(8-task.length+1)) + list(range(11,24-task.length+1)):
        cornellasserts.assert_equals(True, a3_todo.space_available(d, task, h))

    # 5. space not available that would overlap `added`
    for h in [7,8,9,10]:
        cornellasserts.assert_equals(False, a3_todo.space_available(d, task, h))

    # 6. space available for a 13-hour task after `added`
    task = a3_classes.Task("test", 13)
    cornellasserts.assert_equals(True, a3_todo.space_available(d, task, 11))

    # 7. space not available for a 14-hour task after `added`
    task = a3_classes.Task("test", 14)
    cornellasserts.assert_equals(False, a3_todo.space_available(d, task, 11))

    # 8. space available for a Task that take up all time just before `added`
    task = a3_classes.Task("test", 8)
    cornellasserts.assert_equals(True, a3_todo.space_available(d, task, 0))


    # Tests for a Day with multiple Tasks already in it

    added2 = a3_classes.Task("added2, 15:00-18:00", 3)
    for h in [15,16,17]:
        d.time_slots[h] = added2
        d.num_tasks_scheduled = d.num_tasks_scheduled + 1

    # 9. space available for a Task that could fit between the Tasks

    task = a3_classes.Task("test", 2)
    for h in [11, 12, 13]:
        cornellasserts.assert_equals(True, a3_todo.space_available(d, task, h))

    # 10. space not available for a Task that wouldn't fit between the Tasks
    task.length = 5
    for h in range(8,16):
        cornellasserts.assert_equals(False, a3_todo.space_available(d, task, h))


def test_add_task():
    """
    Testing a3_todo.add_task, using roughly the A3 diagram setup as
    a test case.

    For assignment purposes, we have not provided a complete set of tests.
    """
    print("Running test_add_task")

    #1: successful add in middle of completely empty day
    a3_todo.add_task(DAY_POOL[0], predef1, 3)

    #2: successful add to middle of gap in day
    a3_todo.add_task(DAY_POOL[0], predef4, 10)

    #3: successful add going up to the very end of a day
    a3_todo.add_task(DAY_POOL[0], predef3, 21)

    #4: successful add to very beginning of completely empty day
    a3_todo.add_task(DAY_POOL[1], predef2, 0)

    #5: successful add of task filling an entire empty day
    a3_todo.add_task(DAY_POOL[3], predef5, 0)

    #6. overlap to the next day
    a3_todo.add_task(DAY_POOL[2], predef4, 21)

    #7.add a task to conflict with another task
    a3_todo.add_task(DAY_POOL[0], predef2, 22)


    #### CHECKS WHETHER RESULT == EXPECTED.  DO NOT DELETE THIS COMMENT.

    # Things that should not have changed
    assert_task_unchanged(predef1, "SPCA shift", 3)
    assert_task_unchanged(predef2, "work-study", 2)
    assert_task_unchanged(predef3, "cure cancer", 3)
    assert_task_unchanged(predef4, "Study for prelims", 4)
    assert_task_unchanged(predef5, "Conquer enemies", 24)
    assert_task_unchanged(todo_call, "Call mom", 1)
    assert_task_unchanged(todo_hack, "Programming sprint", 6)
    cornellasserts.assert_equals(4, len(DAY_POOL))

    # Check day 0
    day0 = DAY_POOL[0]
    cornellasserts.assert_equals("Monday March 2", day0.name)
    cornellasserts.assert_equals(24, len(day0.time_slots))

    for i in list(range(0,3)) + list(range(6,10)) + list(range(14,21)):
        cornellasserts.assert_equals(None, day0.time_slots[i])
    for i in range(3,6):
        cornellasserts.assert_equals(predef1, day0.time_slots[i])
    for i in range(10,14):
        cornellasserts.assert_equals(predef4, day0.time_slots[i])
    for i in range(21,24):
        cornellasserts.assert_equals(predef3, day0.time_slots[i])
    cornellasserts.assert_equals(3, day0.num_tasks_scheduled)

    # Check day 1
    day1 = DAY_POOL[1]
    cornellasserts.assert_equals("Monday March 9", day1.name)
    cornellasserts.assert_equals(24, len(day1.time_slots))
    for empty in range(2,24):
        cornellasserts.assert_equals(None, day1.time_slots[empty])
    for i in range(0,2):
        cornellasserts.assert_equals(predef2, day1.time_slots[i])
    cornellasserts.assert_equals(1, day1.num_tasks_scheduled)

    # Check day 2
    day2 = DAY_POOL[2]
    cornellasserts.assert_equals("Ides of March", day2.name)
    cornellasserts.assert_equals(24, len(day2.time_slots))
    for slot in day2.time_slots:
        cornellasserts.assert_equals(None, slot)
    cornellasserts.assert_equals(0, day2.num_tasks_scheduled)

    # Check day 3
    day3 = DAY_POOL[3]
    cornellasserts.assert_equals("Monday March 16", day3.name)
    cornellasserts.assert_equals(24, len(day3.time_slots))
    for task in day3.time_slots:
        cornellasserts.assert_equals(predef5, task)
    cornellasserts.assert_equals(1, day3.num_tasks_scheduled)


def test_propose_mtg_times():
    """Test space_available."""
    print("Running propose_mtg_times")

    prof1 = a3_classes.Day("MRC")
    prof2 = a3_classes.Day("LL")

    t1 = a3_classes.Task("sleep", 7)
    t2 = a3_classes.Task("sleep", 7)
    for h in range(0,7):
        prof1.time_slots[h] = t1
        prof2.time_slots[h+2] = t2
    prof1.num_tasks_scheduled = prof1.num_tasks_scheduled+1
    prof2.num_tasks_scheduled = prof2.num_tasks_scheduled+1

    appt1 = a3_classes.Task("meet student A", 1)
    prof2.time_slots[14] = appt1
    prof2.num_tasks_scheduled = prof2.num_tasks_scheduled+1
    appt2 = a3_classes.Task("meet student B", 1)
    prof1.time_slots[15] = appt2
    prof1.num_tasks_scheduled = prof1.num_tasks_scheduled+1

    fac_mtg = a3_classes.Task("faculty meeting", 1)
    prof1.time_slots[12] = fac_mtg
    prof1.num_tasks_scheduled = prof1.num_tasks_scheduled+1
    prof2.time_slots[12] = fac_mtg
    prof2.num_tasks_scheduled = prof2.num_tasks_scheduled+1

    s_mtg = a3_classes.Task("senate meeting", 3)
    for h in [18,19]:
        prof1.time_slots[h] = s_mtg
    prof1.num_tasks_scheduled = prof1.num_tasks_scheduled+1

    dinner = a3_classes.Task("dinner", 2)
    for h in [19, 20]:
        prof2.time_slots[19] = dinner
    prof2.num_tasks_scheduled = prof2.num_tasks_scheduled+1

    prep1 = a3_classes.Task("lecture prep", 3)
    prep2 = a3_classes.Task("lab writeup", 1)
    for h in range(21,24):
        prof1.time_slots[h]=prep1
    prof1.num_tasks_scheduled = prof1.num_tasks_scheduled+1
    prof2.time_slots[22]=prep2
    prof2.num_tasks_scheduled = prof2.num_tasks_scheduled+1

    short_task = a3_classes.Task("one-hour", 1)
    expected_short = ['9:00-10:00', '10:00-11:00', '11:00-12:00', '13:00-14:00']
    expected_short.extend(['16:00-17:00', '17:00-18:00', '20:00-21:00'])
    result = a3_todo.propose_mtg_times(prof1, prof2, short_task)
    cornellasserts.assert_equals(expected_short, result)

    # check that order of calendars doesn't matter
    result = a3_todo.propose_mtg_times(prof2, prof1, short_task)
    cornellasserts.assert_equals(expected_short, result)

    task2 = a3_classes.Task("two-hour", 2)
    expected_task2 = ['9:00-11:00', '10:00-12:00', '16:00-18:00']
    result = a3_todo.propose_mtg_times(prof1, prof2, task2)
    cornellasserts.assert_equals(expected_task2, result)

    task3 = a3_classes.Task("big think", 5)
    result = a3_todo.propose_mtg_times(prof1, prof2, task3)
    cornellasserts.assert_equals([], result)


if __name__ == '__main__':
    test_space_available()
    test_add_task()
    test_propose_mtg_times()
    print("All test cases passed.  That's one task done with!")
