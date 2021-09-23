from user_input import new_task, task_list


def request_user():
    print("Welcome to WorkValve, \n\nPlease enter your tasks for today with time in integer format e.g. 20:15 = 2015\n")
    unfinished = True

    while unfinished:
        new_task(task_list)
        print("\nAre you finished entering your tasks for today?")
        answer = None
        while answer not in ("yes", "no"):
            # repeat when user doesn't enter yes or no
            answer = input("Enter yes or no: ")
            if answer == "yes":
                if task_list[-1]:
                    # check if the task list is empty
                    unfinished = False
                else:
                    print("You did not enter any tasks.\n\nPlease enter another task.")
            elif answer == "no":
                print("\nPlease enter another task.")
            else:
                print("Please enter yes or no.")

    """
    check if user is finished entering tasks
    """


def request_calendar():
    print("\nWould you like to implement your google calendar?\n")
    answer = None
    while answer not in ("yes", "no"):
        # repeat when user doesn't enter yes or no
        answer = input("Enter yes or no: ")
        if answer == "yes":
            # add a gcal_connect_function()
            print("\nyour google calendar has been implemented.")
        elif answer == "no":
            print("your google calendar has not been implemented.")
        else:
            print("Please enter yes or no.")

    print("\nYour schedule is as follows:\n")
