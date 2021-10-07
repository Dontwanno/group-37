from classes import Task, TaskList


def new_task(task_list):
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
                priority = int(input("Priority:"))
                start_time = int(input("Start time: "))
                end_time = int(input("End time: "))
                if start_time > 2400 or end_time > 2400:
                    raise ValueError
                # Add task to the task list
                task_list.add_task(Task(start_time, end_time, priority, description, False))
            elif answer == "no":
                description = input("Description: ")
                priority = int(input("Priority:"))
                task_length = int(input("Task length: "))
                # Fit new task
                task_list.fit_task(Task(task_length, 0, priority, description, False))
    except ValueError:
        # if input was not finished, give message and return old task list
        print("Time must be valid and in integer format e.g. 8:45 = 845, 20:15 = 2015.")
        print("Try again.")
        return
    # if everything went smooth, return
    # print("Task stored successfully")
    return
