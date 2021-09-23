def new_task(task_list):
    """
    Allows user to add a new task
    :param task_list: List of existing tasks
    :return: updated task_list
    """
    print("Entering new task:")
    print('--------------------------------------')
    new_task_list = task_list
    try:
        new_task_list[2].append(input("Description: "))
        new_task_list[0].append(int(input("Start time: ")))
        new_task_list[1].append(int(input("End time: ")))
        if new_task_list[0][-1] > 2400 or new_task_list[1] > 2400:
            raise ValueError
    except ValueError:
        # if input was not finished, give message and return old task list
        print("Time must be valid and in integer format e.g. 8:45 = 845, 20:15 = 2015.")
        print("Try again.")
        return task_list
    # if everything went smooth, return new task list
    print("Task stored successfully")
    return new_task_list

