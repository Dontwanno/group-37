from datetime import time, date, timedelta


class Task:
    def __init__(self, start_time, end_time, duration, priority, description,
                 from_g_cal):
        """
        Initializer for class Task
        :param start_time: Time when task starts, type int, format 500 = 5:00
        :param end_time: Time when task ends, type int, format 500 = 5:00
        :param priority: Priority of the task, higher priority = higher numbers
        :param description: Description of the task, type String
        :param from_g_cal: Whether the origin of task is g cal, type bool
        """
        try:
            if (isinstance(start_time, int) and isinstance(end_time, int)
                    and isinstance(priority, int)
                    and isinstance(from_g_cal, bool) and 0 <= start_time < 2400
                    and 0 <= end_time < 2400 and isinstance(description, str)
                    and start_time <= end_time):
                self.start_time = timedelta(hours=start_time // 100,
                                            minutes=start_time % 100)
                self.end_time = timedelta(hours=end_time // 100,
                                          minutes=end_time % 100)
                self.priority = priority
                self.description = description
                self.from_g_cal = from_g_cal
                if duration:
                    self.duration = timedelta(minutes=duration)
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
        self.task_list = []

    def add_task(self, new_task):
        """
        Adds a task to the TaskList object's task_list
        :param new_task: The new task of class Task
        """
        # Make sure that task_list is not empty
        # If new task is before the latest task, insert it on the correct spot. Else put it last
        if self.task_list:
            if new_task.start_time < self.task_list[-1].start_time:
                i = 0
                while new_task.start_time > self.task_list[i].start_time:
                    i += 1
                if not self.overlap(new_task, self.task_list[i]):
                    self.task_list.insert(i, new_task)
                else:
                    print(f"The time of the task you entered overlapped"
                          f" with {self.task_list[i].description}")
                    return
            else:
                if self.overlap(new_task, self.task_list[-1]):
                    print(
                        "The task you entered overlaps with the last task in the list"
                    )
                else:
                    self.task_list.append(new_task)

        else:
            self.task_list.append(new_task)

    def fit_task(self, new_task, start_end):
        """
        Adds a task to the TaskList object's task_list, in the correct time
        :param new_task: The new task of class Task
        :param start_end: List of start [0] and end [1] times
        """
        if self.task_list:
            time_slots = []
            start_day = timedelta(hours=start_end[0] // 100,
                                  minutes=start_end[0] % 100)
            end_day = timedelta(hours=start_end[1] // 100,
                                minutes=start_end[1] % 100)
            tasks_start_end = [[task.start_time, task.end_time]
                               for task in self.task_list]
            tasks_start_end.insert(0, [end_day, start_day])
            print(tasks_start_end)
            for i, task in enumerate(tasks_start_end):
                if i + 1 < len(tasks_start_end):
                    free_time = tasks_start_end[i + 1][0] - task[1]
                    time_slots.append([free_time, task[1]])
                else:
                    time_slots.append(
                        [tasks_start_end[0][0] - task[1], task[1]])
            print(time_slots)
            # slots in time_slots have duration[0] and start_time[1]

            valid_slots = [
                slot for slot in time_slots if new_task.duration <= slot[0]
            ]
            if valid_slots:
                smallest_slot = min(valid_slots)
                self.add_task(
                    Task(
                        int(self.hours_minutes(smallest_slot[1].seconds)),
                        int(
                            self.hours_minutes(smallest_slot[1].seconds) +
                            self.hours_minutes(new_task.duration.seconds)),
                        int(new_task.duration.seconds / 60),
                        new_task.priority,
                        new_task.description,
                        False,
                    ))

            else:
                pass
                # add task to next day

        else:
            self.add_task(
                Task(
                    start_end[0],
                    int(start_end[0] +
                        self.hours_minutes(new_task.duration.seconds)),
                    int(new_task.duration.seconds / 60),
                    new_task.priority,
                    new_task.description,
                    False,
                ))

    def remove_task(self, removed_task):
        for task in self.task_list:
            if task.description == removed_task:
                self.task_list.remove(task)
                print("Task successfully deleted\n")
                break
        else:
            print("There are no tasks with this description\n")

    def get_task_list(self):
        return self.task_list

    @staticmethod
    def overlap(task1, task2):
        return max(task1.start_time, task2.start_time) < min(
            task1.end_time, task2.end_time)

    @staticmethod
    def hours_minutes(seconds):
        seconds = seconds / 60
        return seconds // 60 * 100 + seconds % 60
