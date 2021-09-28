def formatIntToTimeString(timeInt):
    hour = str(timeInt)[0: len(str(timeInt)) - 2]
    min = str(timeInt)[len(str(timeInt)) - 2: len(str(timeInt))]
    return hour + ':' + min


def displaySchedule(task_list):
    temp_task_list = task_list.get_task_list()
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('SCHEDULE:')
    for i in range(len(temp_task_list)):
        print('- ' + formatIntToTimeString(temp_task_list[i].get_start_time()) + ' --> ' +
              formatIntToTimeString(temp_task_list[i].get_end_time()) + ': ' + temp_task_list[i].get_description())
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    del temp_task_list
