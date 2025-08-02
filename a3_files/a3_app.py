"""
A script application to demonstrate how the functions in a3_todo_list
can be used.

Authors: William Xiao (wmx2) and Lillian Lee (ljl2)
         w/input from Kevin Cook (kjc244), Rhea Bansal (rab378), and Lillian Lee

Version: Mar 1, 2020
"""
import a3_classes
import a3_todo

# Initializing constants to use later
SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6

# if should print out all days
ALL_DAYS = 7


# A dictionary for easy conversion between strings and indices into week list
day_map = {
    'sunday': SUNDAY,
    'monday': MONDAY,
    'tuesday': TUESDAY,
    'wednesday': WEDNESDAY,
    'thursday': THURSDAY,
    'friday': FRIDAY,
    'saturday': SATURDAY
}

# The week containing the days we will use to plan
day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday']
WEEK = [a3_classes.Day(day) for day in day_names]


def sirialize_days(day_list):
    """
    Prints out the tasks for each day in day_list, first by day in the order
    in which they appear in day_list, and then chronologically within each day.

    Parameter day_list: The list of days to print data out for.
    Precondition: day_list is non-empty list of Day objects (no None objects).
    """
    for day in day_list:
        a3_todo.sirialize(day)
        print()


def quit_if_input(s):
    """
    Quits Python if s is either 'q' or 'quit', printing a goodbye in the process.

    Parameter s: the string to check.
    Precondition: s is a string.
    """
    if s in ['q', 'quit']:
        print('Goodbye!')
        quit()


def parse_print(s):
    """
    Returns: the day constant to print out if `s` corresponds to a user input
    for printing out the calendar, ALL_DAYS if we should print out the schedule
    for all days, or -1 otherwise.

    Parameter s: the user input to parse.
    Precondition: s is a string, stripped and lowercased.
    """
    last = s.split(' ')[-1]
    if last in day_map:
        return day_map[last]
    if last == 'all':
        return ALL_DAYS
    return -1


def add_task_to_week():
    """
    Prompts user input get new task info, and then add that task to the
    to-do list (if possible).
    """
    name = input('What is the name of your task? \n> ')
    msg = 'How many hours will your task take (integers please)? \n> '
    length = input(msg).strip().lower()
    while not length.isnumeric():
        print("Sorry, that's not a valid number!")
        length = input(msg).strip().lower()

    new_task = a3_classes.Task(name, int(length))
    msg = 'What day would you like to add this task to? \n> '
    day = input(msg).strip().lower()
    while day not in day_map:
        print("Sorry, that's not a valid day!")
        day = input(msg).strip().lower()

    msg = 'What hour will your task start (24 hour time please)? \n> '
    start = input(msg).strip().lower()
    while not start.isnumeric() and not (0 <= start < 24):
        print("Sorry, that's not a valid hour!")
        start = input(msg).strip().lower()

    if not a3_todo.add_task(WEEK[day_map[day]], new_task, int(start)):
        print("Sorry, couldn't add it to your schedule at that time!")
    else:
        print("Successfully added!")


if __name__ == '__main__':
    welcome = "Welcome to the Tre1110 planner!\n"
    welcome += "Here, you can plan out the next week (from Sunday - Saturday).\n"
    welcome += "Type 'print <day>' to view your schedule for that day, or 'print all'\n"
    welcome += 'to view your whole week at once.\n'
    welcome += "To add a task to the planner, type 'add task'.\n"
    welcome += "Type 'q' to quit.\n"
    welcome += "What would you like to do?"
    print(welcome)

    msg = input('> ').strip().lower()
    while msg not in ['q', 'quit']:
        day_num = parse_print(msg)
        if day_num != -1:
            if day_num == ALL_DAYS:
                sirialize_days(WEEK)
            else:
                sirialize(WEEK[day_num])
        elif msg == 'add task':
            add_task_to_week()
        else:
            print("Sorry, your command was not recognized, please try again!")
        print("What would you like to do now? "
              + "(add task, print <day>, print all, q)")
        msg = input('> ').strip().lower()

    print('Goodbye and good luck getting all your tasks done!')
