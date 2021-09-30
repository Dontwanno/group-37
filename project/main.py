from classes import Task, TaskList
from user_input import new_task
import gcal_connect
from project.displaySchedule import display_schedule


def main():
    # Request user to enter tasks:
    # Store list of tasks:

    # Extract list of tasks:

    # Display list of tasks:
    #       List of tasks format (for now): [startTime][endTime][name]
    #                                   eg: [1500][1600][meeting]
    task_list = TaskList()
    task_list.add_task(Task(800, 1000, "Walk my dog", False))
    task_list.add_task(Task(1030, 1345, "Meeting with SEM boys", False))
    task_list.add_task(Task(1345, 1530, "Do my homework", False))
    task_list.add_task(Task(1545, 1800, "Crying session", False))

    #temporary_list = gcal_connect.get_google_calander(temporary_list)
    new_task(task_list)
    display_schedule(task_list)


if __name__ == '__main__':
    main()
