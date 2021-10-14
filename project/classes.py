from datetime import timedelta
import pickle


class Task:
    def __init__(self, start_time, end_time, duration, priority, description,
                 from_g_cal):
        """
        Initializer for class Task
        :param start_time: Time when task starts, type int, format 500 = 5:00
        :param end_time: Time when task ends, type int, format 500 = 5:00
        :param duration: End_time - start_time
        :param priority: Priority of the task, higher priority = higher numbers
        :param description: Description of the task, type String
        :param from_g_cal: Whether the origin of task is g cal, type bool
        """
        try:
            # print(start_time, isinstance(start_time, timedelta), "isinstance(start_time, timedelta)")
            # print(isinstance(end_time, timedelta), "isinstance(end_time, timedelta)")
            # print(isinstance(from_g_cal, bool), "isinstance(from_g_cal, bool)")
            # print(timedelta(hours=0) <= start_time < timedelta(days=1),
            #       "timedelta(hours=0) < start_time < timedelta(days=1)")
            # print(timedelta(hours=0) <= end_time < timedelta(days=1),
            #       "timedelta(hours=0) < end_time < timedelta(days=1),")
            # print(isinstance(description, str), "isinstance(description, str)")
            # print(start_time <= end_time, "start_time <= end_time")
            # print(duration)
            if all([isinstance(start_time, timedelta), isinstance(end_time, timedelta)
                    , isinstance(from_g_cal, bool), timedelta(hours=0) <= start_time < timedelta(days=1)
                    , timedelta(hours=0) <= end_time < timedelta(days=1), isinstance(description, str)
                    , start_time <= end_time]):
                self.start_time = start_time
                self.end_time = end_time
                self.priority = priority
                self.description = description
                self.from_g_cal = from_g_cal
                if duration:
                    self.duration = duration
                else:
                    self.duration = self.end_time - self.start_time
            else:
                raise TypeError
        except TypeError:
            print(
                "The parameters passed are not of right type.  "
                "start_time and end_time must be int and from_g_cal must be bool."
            )


class TaskList:
    def __init__(self):
        self.task_list_dict = {}

    def add_task(self, new_task, task_date):
        """
        Adds a task to the TaskList object's task_list
        :param task_date: Date-key to the dictionary for the list of tasks on that day
        :param new_task: The new task of class Task
        """
        try:
            if isinstance(new_task, Task):
                # If the date already exists, use the date of that task list
                # Else create task list for that date
                if task_date in self.task_list_dict:
                    task_list = self.task_list_dict[task_date]
                else:
                    self.task_list_dict[task_date] = []
                    task_list = self.task_list_dict[task_date]

                # Make sure that task_list is not empty
                # If new task is before the latest task, insert it on the correct spot. Else put it last
                if task_list:
                    if new_task.start_time < task_list[-1].start_time:
                        i = 0
                        while new_task.start_time > task_list[i].start_time:
                            i += 1
                        if not self.overlap(new_task, task_list[i]) and not self.overlap(new_task, task_list[i-1]):
                            self.task_list_dict[task_date].insert(i, new_task)
                        else:
                            print(f"The time of the task you entered overlapped with another task\nTask was not added.")
                        return
                    else:
                        if self.overlap(new_task, task_list[-1]):
                            print(
                                "The task you entered overlaps with the last task in the list"
                            )
                        else:
                            task_list.append(new_task)
                else:
                    task_list.append(new_task)
            else:
                raise TypeError
        except TypeError:
            print("Task is not off class Task.")

    def fit_task(self, new_task, start_end, task_date):
        """
        Adds a task to the TaskList object's task_list_dict, in the correct time
        :param task_date: Date-key to list of tasks of that day
        :param new_task: The new task of class Task
        :param start_end: List of start [0] and end [1] times
        """
        try:
            if isinstance(new_task, Task):
                if task_date in self.task_list_dict:
                    task_list = self.task_list_dict[task_date]
                else:
                    self.task_list_dict[task_date] = []
                    task_list = self.task_list_dict[task_date]

                start_day = timedelta(hours=start_end[0] // 100,
                                      minutes=start_end[0] % 100)
                end_day = timedelta(hours=start_end[1] // 100,
                                    minutes=start_end[1] % 100)
                if self.task_list_dict[task_date]:
                    time_slots = []
                    tasks_start_end = [[task.start_time, task.end_time]
                                       for task in task_list]
                    tasks_start_end.insert(0, [end_day, start_day])
                    # print(tasks_start_end)
                    for i, task in enumerate(tasks_start_end):
                        if i + 1 < len(tasks_start_end):
                            free_time = tasks_start_end[i + 1][0] - task[1]
                            time_slots.append([free_time, task[1]])
                        else:
                            time_slots.append(
                                [tasks_start_end[0][0] - task[1], task[1]])
                    # print(time_slots)
                    # slots in time_slots have duration[0] and start_time[1]

                    valid_slots = [
                        slot for slot in time_slots if new_task.duration <= slot[0]
                    ]
                    if valid_slots:
                        smallest_slot = min(valid_slots)
                        self.add_task(
                            Task(
                                smallest_slot[1],
                                smallest_slot[1] + new_task.duration,
                                new_task.duration.seconds,
                                new_task.priority,
                                new_task.description,
                                False
                            ), task_date)

                    else:
                        self.fit_task(new_task, start_end, task_date + timedelta(days=1))
                        # try again to fit task in next day
                # If the day is empty, add the task to the start of the day
                else:
                    self.add_task(
                        Task(
                            start_day,
                            start_day + new_task.duration,
                            new_task.duration.seconds,
                            new_task.priority,
                            new_task.description,
                            False
                        ), task_date)
            else:
                raise TypeError
        except TypeError:
            print("Task is not off class Task.")

    def remove_task(self, removed_task):
        """
        This function lets the user remove a task
        :param removed_task: the description of the task the user wants to remove
        :return: edits the task list by deleting the right task
        """
        for task_date in self.task_list_dict:
            for task in self.task_list_dict[task_date]:
                if task.description == removed_task:
                    self.task_list_dict[task_date].remove(task)
                    print("Task successfully deleted\n")
                    return

        print("There are no tasks with this description\n")

    def get_task_list(self):
        return self.task_list_dict

    def read_save_file(self):
        with open('savefile.dat', 'rb') as file:
            self.task_list_dict = pickle.load(file)
        print(self.task_list_dict)

    def save_to_file(self):
        # save to a save file before system exit
        save_list = self.get_task_list()
        with open('savefile.dat', 'wb') as file:
            pickle.dump(save_list, file, protocol=2)
        print(self.task_list_dict)

    @staticmethod
    def overlap(task1, task2):
        return max(task1.start_time, task2.start_time) < min(
            task1.end_time, task2.end_time)
