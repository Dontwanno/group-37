from project.displaySchedule import displaySchedule


def main():
    # Request user to enter tasks:

    # Store list of tasks:

    # Extract list of tasks:

    # Display list of tasks:
    #       List of tasks format (for now): [startTime][endTime][name]
    #                                   eg: [1500][1600][meeting]
    temporary_list = [[845, 1045, 1345, 1545], [1030, 1230, 1530, 1800], ['Walk my dog', 'Meeting with SEM boys', 'Do my homework', 'Crying session']]
    displaySchedule(temporary_list)


if __name__ == '__main__':
        main()
