from project.menu import menu_handler, sigint_handler
import signal
from classes import Task, TaskList


def main():
    x = menu_handler()
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        # os.system('cls')
        x.menuExecution()


if __name__ == '__main__':
        main()
