def set_start_end_time(start_end):
    print("Please enter the start and end time of your workday.\n")
    start_time = input("Start time: ")
    end_time = input("End time: ")
    print(f"\nThe start time you entered is: {start_time[:2]}:{start_time[2:]}\nThe end time you entered is:"
          f" {end_time[:2]}:{end_time[2:]}\nAre these times correct?")
    start_end[0] = int(start_time)
    start_end[1] = int(end_time)
    answer = None
    while answer not in ("yes", "no"):
        # repeat when user doesn't enter yes or no
        answer = input("Enter yes or no: ")
        if answer == "yes":
            return
        elif answer == "no":
            set_start_end_time(start_end)
        else:
            print("Please enter yes or no.")

# set_start_end_time()
# print(start_end)
