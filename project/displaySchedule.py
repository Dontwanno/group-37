def format_int_to_time_string(time_int):
    hour = str(time_int)[0: len(str(time_int)) - 2]
    min = str(time_int)[len(str(time_int)) - 2: len(str(time_int))]
    return hour + ':' + min


def display_schedule(task_list):
    temp_task_list = task_list.get_task_list()
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('SCHEDULE:')
    for i in range(len(temp_task_list)):
        print('- ' + format_int_to_time_string(temp_task_list[i].get_start_time()) + ' --> ' +
              format_int_to_time_string(temp_task_list[i].get_end_time()) + ': ' + temp_task_list[i].get_description())
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    del temp_task_list
