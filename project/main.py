from project.displaySchedule import display_schedule
from console_user_interface import request_user, request_calendar
from user_input import new_task
from classes import Task, TaskList
import gcal_connect


def main():
    # Request user to enter tasks:
    #request_user()
    #request_calendar()
    # Store list of tasks:

    # Extract list of tasks:

    # Display list of tasks:
    #       List of tasks format (for now): [startTime][endTime][name]
    #                                   eg: [1500][1600][meeting]
    task_list = TaskList()
    task_list.add_task(Task(800,  1000, 1,  "Walk my dog", False))
    task_list.add_task(Task(1030, 1345, 1,  "Meeting with SEM boys", False))
    task_list.add_task(Task(1345, 1530, 1,  "Do my homework", False))
    task_list.add_task(Task(1545, 1800, 1,  "Crying session", False))

    #temporary_list = gcal_connect.get_google_calander(temporary_list)
    new_task(task_list)
    display_schedule(task_list)


if __name__ == '__main__':
        main()
