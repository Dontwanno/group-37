#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :Simple Python Menu
# description     :Template for a custom scripting menu
# author          :@cortesjorgea
# date            :10/2018
# updated         :04/2020
# version         :2.0
# usage           :simple_python_menu.py
# notes           :Update section USER CONFIG dicts and reimplement methods
#                 of main_menu and view_tasks classes at BACKEND section.
# python_version  :3.8.0
# =======================================================================
import sys, os, signal, colorama
from displaySchedule import display_schedule
from user_input import new_task
from classes import Task, TaskList
import gcal_connect
from start_end_time import set_start_end_time

start_end = [1000, 2000]
task_list = TaskList()
task_list.add_task(Task(845, 1030, "Walk my dog", False))
task_list.add_task(Task(1030, 1345, "Meeting with SEM boys", False))
task_list.add_task(Task(1345, 1530, "Do my homework", False))
task_list.add_task(Task(1545, 1800, "Crying session", False))

colorama.init()  # Color init for Windows

# =======================
#    DEFINES
# =======================

colors = {
    "info": "35m",  # Orange for info messages
    "error": "31m",  # Red for error messages
    "ok": "32m",  # Green for success messages
    "view_tasksc": "\033[46m",  # Light blue menu
    "main_menuc": "\033[44m",  # Blue menu
    "close": "\033[0m"  # Color coding close
}
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["main_menuc"]
c2 = colors["view_tasksc"]

# =======================
#    USER CONFIG
# =======================
programtitle = "WorkValve"

# Fill the options as needed.
main_menu_colors = {
    "ct": ct,
    "cs": cs,
    "opt": c1
}
main_menu_options = {
    "title": "Main menu",
    "1": "Add tasks",
    "2": "View tasks",
    "3": "Settings",
    "0": "Quit (or use CNTRL+C)",
}

view_tasks_colors = {
    "ct": ct,
    "cs": cs,
    "opt": c2
}
view_tasks_options = {
    "title": "View tasks",
    "1": "View tasks ",
    "2": "Main menu",
    "0": "Quit (or use CNTRL+C)",
}

add_tasks_colors = {
    "ct": ct,
    "cs": cs,
    "opt": c2
}
add_tasks_options = {
    "title": "Add/Remove tasks",
    "1": "Add task",
    "2": "Remove task",
    "3": "Main menu",
    "0": "Quit (or use CNTRL+C)",
}

settings_colors = {
    "ct": ct,
    "cs": cs,
    "opt": c1
}
settings_options = {
    "title": "Settings",
    "1": "Change start and end time of day",
    "2": "Show current start and end time of day",
    "3": "Main menu",
    "0": "Quit (or use CNTRL+C)",
}


# =======================
#      HELPERS
# =======================
def printWithColor(color, string):
    print("\033[" + colors[color] + " " + string + cc)


def printError():
    printWithColor("error", "Error!!")
    return 1


def printSuccess():
    printWithColor("ok", "Success!!")
    return 0


# Exit program
def exit():
    sys.exit()


# Handles the CNTRL+C to leave properly the script
def sigint_handler(signum, frame):
    print("CNTRL+C exit")
    sys.exit(0)


# =======================
#      ACTIONS
# =======================

# Menu template
class menu_template():

    def __init__(self, options, colors):
        self.menu_width = 50  # Width in characters of the printed menu
        self.options = options
        self.colors = colors

    # =======================
    #      Menu prints
    # =======================
    def createMenuLine(self, letter, color, length, text):
        menu = color + " [" + letter + "] " + text
        line = " " * (length - len(menu))
        return menu + line + cc

    def createMenu(self, size):
        line = self.colors["ct"] + " " + programtitle
        line += " " * (size - len(programtitle) - 6)
        line += cc
        print(line)  # Title
        line = self.colors["cs"] + " " + self.options["title"]
        line += " " * (size - len(self.options["title"]) - 6)
        line += cc
        print(line)  # Subtitle
        for key in self.options:
            if (key != "title"):
                print(self.createMenuLine(key, self.colors["opt"], size, self.options[key]))

    def printMenu(self):
        self.createMenu(self.menu_width)

    # =======================
    #      Action calls
    # =======================
    def action(self, ch):
        if ch == '1':
            self.method_1()
        elif ch == '2':
            self.method_2()
        elif ch == '3':
            self.method_3()
        elif ch == '4':
            self.method_4()
        elif ch == '5':
            self.method_5()
        elif ch == 'a':
            self.method_a()
        elif ch == 's':
            self.method_s()
        elif ch == 'd':
            self.method_d()
        elif ch == 'e':
            self.method_e()
        elif ch == 'f':
            self.method_f()
        elif (ch == ''):
            pass  # Print menu again
        elif ch == '0':
            sys.exit()
        else:
            printError()

    # =======================
    #      Empty methods
    # =======================
    def method_1(self):
        pass

    def method_2(self):
        pass

    def method_3(self):
        pass

    def method_4(self):
        pass

    def method_5(self):
        pass

    def method_a(self):
        pass

    def method_s(self):
        pass

    def method_d(self):
        pass

    def method_e(self):
        pass

    def method_f(self):
        pass


# =======================
#      BACKEND
# =======================

# Create here custom actions.

class main_menu(menu_template):
    pass


class add_tasks(menu_template):
    def method_1(self):
        new_task(task_list)
        return

    def method_2(self):
        return


class view_tasks(menu_template):
    def method_1(self):
        display_schedule(task_list)
        return


class settings(menu_template):
    def method_1(self):
        set_start_end_time(start_end)

    def method_2(self):
        start_time = str(start_end[0])
        end_time = str(start_end[1])
        print(f"Your start time is: {start_time[:2]}:{start_time[2:]} and your end time is:"
          f" {str(end_time)[:2]}:{end_time[2:]}")


# =======================
#      MAIN PROGRAM
# =======================

class menu_handler:

    def __init__(self):
        self.current_menu = "main_menu"
        self.m1 = main_menu(main_menu_options, main_menu_colors)
        self.m2 = add_tasks(add_tasks_options, add_tasks_colors)
        self.m3 = view_tasks(view_tasks_options, view_tasks_colors)
        self.m4 = settings(settings_options, settings_colors)

    def menuExecution(self):
        if (self.current_menu == "main_menu"):
            self.m1.printMenu()
        elif (self.current_menu == "add_tasks"):
            self.m2.printMenu()
        elif (self.current_menu == "view_tasks"):
            self.m3.printMenu()
        elif (self.current_menu == "settings"):
            self.m4.printMenu()

        choice = input("Please enter what you want to do: ")
        if (self.current_menu == "main_menu"):
            if (choice == "1"):
                self.current_menu = "add_tasks"
            elif (choice == "2"):
                self.current_menu = "view_tasks"
            elif (choice == "3"):
                self.current_menu = "settings"
            else:
                self.actuator(0, choice)

        elif (self.current_menu == "add_tasks"):
            if (choice == "3"):
                self.current_menu = "main_menu"
            else:
                self.actuator(1, choice)

        elif (self.current_menu == "view_tasks"):
            if (choice == "2"):
                self.current_menu = "main_menu"
            else:
                self.actuator(2, choice)

        elif self.current_menu == "settings":
            if (choice == "3"):
                self.current_menu = "main_menu"
            else:
                self.actuator(3, choice)

    def actuator(self, type, ch):
        if type == 0:
            self.m1.action(ch)
        elif type == 1:
            self.m2.action(ch)
        elif type == 2:
            self.m3.action(ch)
        elif type == 3:
            self.m4.action(ch)


# Main Program
# if __name__ == "__main__":
x = menu_handler()
signal.signal(signal.SIGINT, sigint_handler)
while True:
    # os.system('cls')
    x.menuExecution()
