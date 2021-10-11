import signal
from project.menu import MenuHandler, sigint_handler
# from classes import Task, TaskList


def main():
    handler = MenuHandler()
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        # os.system('cls')
        handler.menu_execution()


if __name__ == '__main__':
    main()
