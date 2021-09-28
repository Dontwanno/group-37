class Task:
    def __init__(self, start_time, end_time, description, from_g_cal):
        """
        Initializer for class Task
        :param start_time: Time when task starts, type int, format 500 = 5:00
        :param end_time: Time when task ends, type int, format 500 = 5:00
        :param description: Description of the task, type String
        :param from_g_cal: Whether the origin of task is g cal, type bool
        """
        try:
            if isinstance(start_time, int) and isinstance(end_time, int) and isinstance(from_g_cal, bool)\
                    and 0 <= start_time < 2400 and 0 <= end_time < 2400 and isinstance(description, str):
                self.start_time = start_time
                self.end_time = end_time
                self.description = description
                self.from_g_cal = from_g_cal
            else:
                raise TypeError
        except TypeError:
            print("The parameters passed are not of right type. start_time and end_time must be int and from_g_cal "
                  "must be bool.")

    def get_end_time(self):
        return self.end_time

    def get_start_time(self):
        return self.start_time

    def get_description(self):
        return self.description

    def get_from_g_cal(self):
        return self.from_g_cal


class TaskList:
    def __init__(self):
        self.task_list = []

    def add_task(self, new_task):
        """
        Adds a task to the TaskList object's task_list
        :param new_task: The new task of class Task
        """
        try:
            if isinstance(new_task, Task):
                # Make sure that task_list is not empty
                # If new task is before the latest task, insert it on the correct spot
                if self.task_list and new_task.get_start_time() < self.task_list[len(self.task_list) - 1].get_start_time():
                    i = 0
                    while new_task.get_start_time() > self.task_list[i].get_start_time():
                        i += 1
                    self.task_list.insert(i, new_task)
                else:
                    self.task_list.append(new_task)
            else:
                raise TypeError
        except TypeError:
            print("Task is not of class Task.")

    def get_task_list(self):
        return self.task_list
