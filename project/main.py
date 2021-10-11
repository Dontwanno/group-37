from project.menu import MenuHandler, sigint_handler
import signal
from classes import Task, TaskList

def main():
    x = MenuHandler()
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        # os.system('cls')
        x.menu_execution()


if __name__ == '__main__':
    main()
