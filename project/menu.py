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
import sys, colorama
from ui import new_task, display_schedule, set_start_end_time
from classes import Task, TaskList
from apis import get_google_calendar

task_list = TaskList()
# Get current tasks from Google
# task_list = get_google_calendar(task_list)
start_end = [1000, 2000]


colorama.init()  # Color init for Windows

# =======================
#    DEFINES
# =======================

colors = {
    "info": "35m",  # Orange for info messages
    "error": "31m",  # Red for error messages
    "ok": "32m",  # Green for success messages
    "other_menus": "\033[46m",  # Light blue menu
    "main_menu": "\033[44m",  # Blue menu
    "close": "\033[0m"  # Color coding close
}
CC = "\033[0m"
CT = "\033[101m"
CS = "\033[41m"
C1 = colors["main_menu"]
C2 = colors["other_menus"]

# =======================
#    USER CONFIG
# =======================
PROGRAM_TITLE = "WorkValve"

# Fill the options as needed.
main_menu_colors = {
    "ct": CT,
    "cs": CS,
    "opt": C1
}
main_menu_options = {
    "title": "Main menu",
    "1": "Add/Remove tasks",
    "2": "View tasks",
    "3": "Settings",
    "0": "Quit (or use CNTRL+C)",
}

view_tasks_colors = {
    "ct": CT,
    "cs": CS,
    "opt": C2
}
view_tasks_options = {
    "title": "View tasks",
    "1": "View tasks ",
    "2": "Main menu",
    "0": "Quit (or use CNTRL+C)",
}

add_tasks_colors = {
    "ct": CT,
    "cs": CS,
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
    "ct": CT,
    "cs": CS,
    "opt": C2
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


def print_error(error_message):
    print_with_color("error", error_message)
    return 1


def print_success():
    print_with_color("ok", "Success!!")
    return 0


# Exit program
def menu_exit():
    sys.exit()


# Handles the CNTRL+C to leave properly the script
def sigint_handler():
    print("CNTRL+C exit")
    sys.exit(0)


# =======================
#      ACTIONS
# =======================

# Menu template
class MenuTemplate:

    def __init__(self, options, colours):
        self.menu_width = 50  # Width in characters of the printed menu
        self.options = options
        self.colors = colours
        self.method_dict = {"1": self.method_1,
                            "2": self.method_2,
                            "3": self.method_3,
                            "4": self.method_4,
                            "5": self.method_5,
                            "a": self.method_a,
                            "s": self.method_s,
                            "d": self.method_d,
                            "e": self.method_e,
                            "f": self.method_f,
                            "0": self.method_0
                            }

    # =======================
    #      Menu prints
    # =======================

    def create_menu_line(self, letter, color, length, text):
        menu = color + " [" + letter + "] " + text
        line = " " * (length - len(menu))
        return menu + line + CC

    def create_menu(self, size):
        line = self.colors["ct"] + " " + PROGRAM_TITLE
        line += " " * (size - len(PROGRAM_TITLE) - 6)
        line += CC
        print(line)  # Title
        line = self.colors["cs"] + " " + self.options["title"]
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
        if choice in self.method_dict:
            self.method_dict[choice]()
        elif choice == "":
            pass
        else:
            print_error("Please enter valid menu option")

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

    def method_0(self):
        sys.exit()


# =======================
#      BACKEND (instantiation of all the different menus)
# =======================

# Create here custom actions.

class MainMenu(MenuTemplate):
    def method_1(self):
        MenuHandler.current_menu = "add_tasks"

    def method_2(self):
        MenuHandler.current_menu = "view_tasks"

    def method_3(self):
        MenuHandler.current_menu = "settings"


class AddTasks(MenuTemplate):
    def method_1(self):
        new_task(task_list, start_end)

    def method_2(self):
        remove_task(task_list)
        return

    def method_3(self):
        MenuHandler.current_menu = "main_menu"


class ViewTasks(MenuTemplate):
    def method_1(self):
        display_schedule(task_list)

    def method_2(self):
        MenuHandler.current_menu = "main_menu"


class Settings(MenuTemplate):
    def method_1(self):
        set_start_end_time(start_end)

    def method_2(self):
        start_time = str(start_end[0])
        end_time = str(start_end[1])
        print(f"Your start time is: {start_time[:2]}:{start_time[2:]} and your end time is:"
              f" {str(end_time)[:2]}:{end_time[2:]}")

    def method_3(self):
        MenuHandler.current_menu = "main_menu"


# =======================
#      MAIN PROGRAM
# =======================

# set initial menu

class MenuHandler:
    current_menu = "main_menu"

    def __init__(self):

        self.menu_dict = {"main_menu": MainMenu(main_menu_options, main_menu_colors),
                          "add_tasks": AddTasks(add_tasks_options, add_tasks_colors),
                          "view_tasks": ViewTasks(view_tasks_options, view_tasks_colors),
                          "settings": Settings(settings_options, settings_colors)}

    def menu_execution(self):
        self.menu_dict[MenuHandler.current_menu].print_menu()
        choice = input("Please enter what you want to do: ")
        self.menu_dict[MenuHandler.current_menu].action(choice)
