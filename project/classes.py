class Task:
    def __init__(self, start_time, end_time, priority, description, from_g_cal):
        """
        Initializer for class Task
        :param start_time: Time when task starts, type int, format 500 = 5:00
        :param end_time: Time when task ends, type int, format 500 = 5:00
        :param priority: Priority of the task, higher priority = higher numbers
        :param description: Description of the task, type String
        :param from_g_cal: Whether the origin of task is g cal, type bool
        """
        try:
            if isinstance(start_time, int) and isinstance(end_time, int) and isinstance(priority, int) and isinstance(from_g_cal, bool)\
                    and 0 <= start_time < 2400 and 0 <= end_time < 2400 and isinstance(description, str):
                self.start_time = start_time
                self.end_time = end_time
                self.priority = priority
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

    def get_priority(self):
        return self.priority

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

    def fit_task(self, new_task):
        """
        Adds a task to the TaskList object's task_list
        :param new_task: The new task of class Task
        """
        try:
            if isinstance(new_task, Task):
                # Make sure that task_list is not empty

                task_length = new_task.get_start_time()

                # Determine spot to fit task
                # For now, workday hardcoded from 6am -> 7pm
                workday = [800, 1900]
                free_time_list = [[]]
                free_time_list[0] = [workday[0], workday[1]]
                print(str(len(free_time_list)))
                for task in self.get_task_list():
                    #print(task.get_start_time())
                    #remove_overlap(task, )

                    for slot in free_time_list:
                        #Check if starttime fits in interval
                        if slot[0] <= task.get_start_time() < slot[1] <= task.get_end_time():
                            # Shorten free time slot
                            slot[1] = task.get_start_time()
                            #print('Removed last part free time slot!')
                        elif task.get_start_time() <= slot[0] < task.get_end_time() < slot[1]:
                            # Shorten free time slot
                            slot[0] = task.get_end_time()
                            #print('Removed first part free time slot!')
                        elif slot[0] <= task.get_start_time() < task.get_end_time() < slot[1]:
                            # Split free time slot
                            tmp_free_slot_endtime = slot[1]
                            slot[1] = task.get_start_time()
                            free_time_list.append([task.get_end_time(), tmp_free_slot_endtime])
                            #print('Appended free time slot!')
                        elif task.get_start_time() < task.get_end_time() <= slot[0]:
                            # Continue, no overlap
                            print("Task before slot, no overlap!")
                        elif slot[1] <= task.get_start_time() < task.get_end_time():
                            # Continue, no overlap
                            print("Task after slot, no overlap!")
                        else:
                            # Remove free time slot
                            #del free_time_list[0]
                            free_time_list.remove(slot)
                            #print('Removed free time slot!')

                i = 0
                while i < len(free_time_list):
                    print(str(free_time_list[i][0]) + " -> " + str(free_time_list[i][1]))
                    i += 1

                found_slot = False
                i = 0
                for slot in free_time_list:
                    start_hour = int(str(slot[0])[0: len(str(slot[0])) - 2])
                    start_min = int(str(slot[0])[len(str(slot[0])) - 2: len(str(slot[0]))])
                    end_hour = int(str(slot[1])[0: len(str(slot[1])) - 2])
                    end_min = int(str(slot[1])[len(str(slot[1])) - 2: len(str(slot[1]))])

                    min_diff = end_min - start_min
                    hour_diff = end_hour - start_hour
                    # Hour difference * 100 in order to shift the number 2 positions left and add minutes
                    if min_diff > 0:
                        time_diff = hour_diff * 100 + min_diff
                    else:
                        time_diff = (hour_diff - 1) * 100 + min_diff + 60
                    print("Length = " + str(time_diff))
                    # slot_length[i] = time_diff
                    if time_diff >= task_length:
                        # Fit task here!!
                        #print("Task length = " + str(task_length))
                        if len(str(task_length)) > 2:
                            task_length_hour = int(str(task_length)[0: len(str(task_length)) - 2])
                        else:
                            task_length_hour = 0
                        #print(task_length_hour)
                        task_length_min = int(str(task_length)[len(str(task_length)) - 2: len(str(task_length))])
                        #print(task_length_min)
                        task_end_hour = int(str(slot[0])[0: len(str(slot[0])) - 2]) + task_length_hour
                        #print(task_end_hour)
                        task_end_min = int(str(slot[0])[len(str(slot[0])) - 2: len(str(slot[0]))]) + task_length_min
                        #print(task_end_min)
                        if task_end_min >= 60:
                            task_end_min -= 60
                            task_end_hour += 1
                        task_end_time = (task_end_hour * 100) + task_end_min
                        fitted_task = Task(slot[0], task_end_time, new_task.get_priority(), new_task.get_description(), new_task.get_from_g_cal())

                        print(fitted_task.get_start_time())
                        print(fitted_task.get_end_time())
                        print(fitted_task.get_priority())
                        print(fitted_task.get_description())
                        print(fitted_task.get_from_g_cal())

                        found_slot = True

                        # Insert task in to list
                        # If new task is before the latest task, insert it on the correct spot
                        if self.task_list and fitted_task.get_start_time() < self.task_list[len(self.task_list) - 1].get_start_time():
                            i = 0
                            while fitted_task.get_start_time() > self.task_list[i].get_start_time():
                                i += 1
                            self.task_list.insert(i, fitted_task)
                        else:
                            self.task_list.append(fitted_task)

                        break
                    i += 1
                if found_slot:
                    print("Found a slot to fit task!")
                else:
                    print("Could not find a slot to fit your task :-(")
            else:
                raise TypeError
        except TypeError:
            print("Task is not of class Task.")

    def get_task_list(self):
        return self.task_list
