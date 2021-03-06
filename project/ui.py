from datetime import date, timedelta
from classes import Task


def new_task(task_list, start_end):
    """
    Allows user to add a new task
    :param task_list: List of existing tasks, class TaskList
    :return: nothing. TaskList object got updated
    """
    print("Entering new task:")
    print('--------------------------------------')

    try:
        print('Would you like to enter the start and end time for your task?')
        answer = None
        while answer not in ("yes", "no"):
            # repeat when user doesn't enter yes or no
            answer = input("Enter yes or no: ")
            if answer == "yes":
                description = input("Description: ")
                # priority = int(input("Priority: "))
                start = int(input("Start time: "))
                end = int(input("End time: "))
                start_time = timedelta(hours=start // 100,
                                       minutes=start % 100)
                end_time = timedelta(hours=end // 100,
                                     minutes=end % 100)
                if is_valid_task(description, False, start, end):
                    # Add task to the task list
                    task_list.add_task(Task(start_time, end_time, None, None, description, False), date.today())
                else:
                    raise ValueError
            elif answer == "no":
                description = input("Description: ")
                priority = int(input("Priority: "))
                task_length = int(input("Task length in minutes: "))
                task_length_delta = timedelta(minutes=task_length)
                # Fit new task
                if is_valid_task(description, False, duration=task_length, priority=1):
                    task_list.fit_task(Task(timedelta(0), timedelta(0), task_length_delta,
                                            priority, description, False), start_end, date.today())
                else:
                    raise ValueError

    except ValueError:
        # if input was not finished, give message and return old task list
        print("Time must be valid and in integer format e.g. 8:45 = 845, 20:15 = 2015.\n"
              "Priority must be integer. Task length must be in minutes and be less than 1440 (24 hours) ")
        return
    # if everything went smooth, return
    # print("Task stored successfully")
    return


def set_start_end_time(start_end):
    '''
    This definition lets the user input a start and end time for their day.
    :param start_end: The current start and end time of the day
    :return: The start and end time entered by the user
    '''
    print("Please enter the start and end time of your workday.\n")
    start_time = input("Start time: ")
    end_time = input("End time: ")
    print(f"\nThe start time you entered is:\
            {start_time[:2]}:{start_time[2:]}\nThe end time you entered is:"
          f" {end_time[:2]}:{end_time[2:]}\nAre these times correct?")
    start_end[0] = int(start_time)
    start_end[1] = int(end_time)
    answer = None
    while answer not in ("yes", "no"):
        # repeat when user doesn't enter yes or no
        answer = input("Enter yes or no: ")
        if answer == "yes":
            return
        elif answer == "no":
            set_start_end_time(start_end)
        else:
            print("Please enter yes or no.")


def format_int_to_time_string(time_int):
    '''
    This definition formats an entered time into a timestring
    :param time_int: The time as an integer
    :return: a time string
    '''
    hour = str(time_int)[0: len(str(time_int)) - 2]
    minutes = str(time_int)[len(str(time_int)) - 2: len(str(time_int))]
    return hour + ':' + minutes


def display_schedule(task_list):
    for date_time in task_list.task_list_dict:
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(f'SCHEDULE: {date_time}')
        for task in task_list.task_list_dict[date_time]:
            print(f"- {task.start_time} --> {task.end_time}: {task.description}")
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')


def get_date(answer=None):
    print('Would you like to remove a task?')
    while answer not in ("yes", "no"):
        # repeat when user doesn't enter yes or no
        answer = input("Enter yes or no: ")
        if answer == "yes":
            try:
                date_input = input("Please enter date in format 'day month year' e.g. 13 3 2000: ")
                date_input = date_input.split()
                date_input = [int(x) for x in date_input]
                if len(date_input) == 2:
                    date_input.append(date.today().year)
                return date(date_input[2], date_input[1], date_input[0])
            except (ValueError, IndexError):
                print("Please enter a valid date")
        elif answer == "no":
            return date.today()
        else:
            print("Please enter 'yes' or 'no'")


def remove_task(task_list):
    """
    Allows user to remove a task
    :param task_list: List of existing tasks, class TaskList
    """
    print('Would you like to remove a task?')
    answer = None
    while answer not in ("yes", "no"):
        # repeat when user doesn't enter yes or no
        answer = input("Enter yes or no: ")
        if answer == "yes":
            display_schedule(task_list)
            removed_task = input("please enter the name of the task you would like to remove: ")
            # remove task from task list
            task_list.remove_task(removed_task)
        elif answer == "no":
            return
        else:
            print("Please enter 'yes' or 'no'")
        return

def is_valid_task(description, from_g_cal, start=0, end=0, duration=1, priority=1):
    return all(
        [
            0 <= start < 2400 and start % 100 < 60,
            start <= end,
            0 <= end < 2400 and end % 100 < 60,
            0 < duration < 2400,
            isinstance(priority, int),
            isinstance(description, str),
            isinstance(from_g_cal, bool),
            ]
    )
