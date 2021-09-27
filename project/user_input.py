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
        entered_task = [[], [], []]
        entered_task[2] = input("Description: ")
        entered_task[0] = int(input("Start time: "))
        entered_task[1] = int(input("End time: "))
        if entered_task[0] > 2400 or entered_task[1] > 2400:
            raise ValueError
    except ValueError:
        # if input was not finished, give message and return old task list
        print("Time must be valid and in integer format e.g. 8:45 = 845, 20:15 = 2015.")
        print("Try again.")
        return task_list
    # If new task is before the latest task, insert it on the correct spot
    if entered_task[0] < task_list[0][len(task_list[0])-1]:
        i = 0
        while entered_task[0] > task_list[0][i]:
            i += 1

        new_task_list[0].insert(i, entered_task[0])
        new_task_list[1].insert(i, entered_task[1])
        new_task_list[2].insert(i, entered_task[2])
    # Otherwise, append it to the list
    else:
        new_task_list[0].append(entered_task[0])
        new_task_list[1].append(entered_task[1])
        new_task_list[2].append(entered_task[2])

    # if everything went smooth, return new task list
    print("Task stored successfully")
    return new_task_list

