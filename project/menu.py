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
import sys
import colorama
from ui import new_task, display_schedule, set_start_end_time
from classes import Task, TaskList
# from api_folder import get_google_calendar

task_list = TaskList()
# Get current tasks from Google
# task_list = get_google_calendar(task_list)
start_end = [1000, 2000]

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
CC = "\033[0m"
CT = "\033[101m"
CS = "\033[41m"
C1 = colors["main_menuc"]
C2 = colors["view_tasksc"]

# =======================
#    USER CONFIG
# =======================
PROGRAMTITLE = "WorkValve"

# Fill the options as needed.
main_menu_colors = {
    "CT": CT,
    "CS": CS,
    "opt": C1
}
main_menu_options = {
    "title": "Main menu",
    "1": "Add tasks",
    "2": "View tasks",
    "3": "Settings",
    "0": "Quit (or use CNTRL+C)",
}

view_tasks_colors = {
    "CT": CT,
    "CS": CS,
    "opt": C2
}
view_tasks_options = {
    "title": "View tasks",
    "1": "View tasks ",
    "2": "Main menu",
    "0": "Quit (or use CNTRL+C)",
}

add_tasks_colors = {
    "CT": CT,
    "CS": CS,
    "opt": C2
}
add_tasks_options = {
    "title": "Add/Remove tasks",
    "1": "Add task",
    "2": "Remove task",
    "3": "Main menu",
    "0": "Quit (or use CNTRL+C)",
}

settings_colors = {
    "CT": CT,
    "CS": CS,
    "opt": C1
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
def print_with_color(color, string):
    print("\033[" + colors[color] + " " + string + CC)


def print_error():
    print_with_color("error", "Error!!")
    return 1


def print_success():
    print_with_color("ok", "Success!!")
    return 0


# Handles the CNTRL+C to leave properly the script
def sigint_handler():
    print("CNTRL+C exit")
    sys.exit(0)


# =======================
#      ACTIONS
# =======================

# Menu template
class MenuTemplate():

    def __init__(self, options, colours):
        self.menu_width = 50  # Width in characters of the printed menu
        self.options = options
        self.colors = colours

    # =======================
    #      Menu prints
    # =======================
    def create_menu_line(self, letter, color, length, text):
        menu = color + " [" + letter + "] " + text
        line = " " * (length - len(menu))
        return menu + line + CC

    def create_menu(self, size):
        line = self.colors["CT"] + " " + PROGRAMTITLE
        line += " " * (size - len(PROGRAMTITLE) - 6)
        line += CC
        print(line)  # Title
        line = self.colors["CS"] + " " + self.options["title"]
        line += " " * (size - len(self.options["title"]) - 6)
        line += CC
        print(line)  # Subtitle
        for key in self.options:
            if key != "title":
                print(self.create_menu_line(key, self.colors["opt"], size, self.options[key]))

    def print_menu(self):
        self.create_menu(self.menu_width)

    # =======================
    #      Action calls
    # =======================
    def action(self, choice):
        if choice == '1':
            self.method_1()
        elif choice == '2':
            self.method_2()
        elif choice == '3':
            self.method_3()
        elif choice == '4':
            self.method_4()
        elif choice == '5':
            self.method_5()
        elif choice == 'a':
            self.method_a()
        elif choice == 's':
            self.method_s()
        elif choice == 'd':
            self.method_d()
        elif choice == 'e':
            self.method_e()
        elif choice == 'f':
            self.method_f()
        elif choice == '':
            pass  # Print menu again
        elif choice == '0':
            sys.exit()
        else:
            print_error()

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

class MainMenu(MenuTemplate):
    pass


class AddTasks(MenuTemplate):
    def method_1(self):
        new_task(task_list, start_end)
        return 0

    def method_2(self):
        return 0


class ViewTasks(MenuTemplate):
    def method_1(self):
        display_schedule(task_list)
        return 0


class Settings(MenuTemplate):
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

class MenuHandler:

    def __init__(self):
        self.current_menu = "main_menu"
        self.m_1 = MainMenu(main_menu_options, main_menu_colors)
        self.m_2 = AddTasks(add_tasks_options, add_tasks_colors)
        self.m_3 = ViewTasks(view_tasks_options, view_tasks_colors)
        self.m_4 = Settings(settings_options, settings_colors)

    def menu_execution(self):
        if self.current_menu == "main_menu":
            self.m_1.print_menu()
        elif self.current_menu == "add_tasks":
            self.m_2.print_menu()
        elif self.current_menu == "view_tasks":
            self.m_3.print_menu()
        elif self.current_menu == "settings":
            self.m_4.print_menu()

        choice = input("Please enter what you want to do: ")
        if self.current_menu == "main_menu":
            if choice == "1":
                self.current_menu = "add_tasks"
            elif choice == "2":
                self.current_menu = "view_tasks"
            elif choice == "3":
                self.current_menu = "settings"
            else:
                self.actuator(0, choice)

        elif self.current_menu == "add_tasks":
            if choice == "3":
                self.current_menu = "main_menu"
            else:
                self.actuator(1, choice)

        elif self.current_menu == "view_tasks":
            if choice == "2":
                self.current_menu = "main_menu"
            else:
                self.actuator(2, choice)

        elif self.current_menu == "settings":
            if choice == "3":
                self.current_menu = "main_menu"
            else:
                self.actuator(3, choice)

    def actuator(self, types, choice):
        if types == 0:
            self.m_1.action(choice)
        elif types == 1:
            self.m_2.action(choice)
        elif types == 2:
            self.m_3.action(choice)
        elif types == 3:
            self.m_4.action(choice)
