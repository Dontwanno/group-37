import pytest

from project.classes import Task, TaskList


def test_task():
    new_task = Task(600, 800, "Swimming", False)
    assert new_task.get_start_time() == 600
    assert new_task.get_end_time() == 800
    assert new_task.get_description() == "Swimming"
    assert not new_task.get_from_g_cal()


def test_task_exception():
    bad_task = Task(100, 200, 100, True)
    with pytest.raises(AttributeError):
        bad_task.get_start_time()


def test_task_list_add_task():
    test_list = TaskList()
    test_list.add_task(Task(100, 200, "test1", False))
    test_task_list = test_list.get_task_list()
    assert len(test_task_list) == 1
    assert test_task_list[-1].get_start_time() == 100
    assert test_task_list[-1].get_end_time() == 200
    assert test_task_list[-1].get_description() == "test1"
    assert not test_task_list[-1].get_from_g_cal()
    test_list.add_task(Task(30, 100, "test2", False))
    assert test_list.get_task_list()[0].get_description() == "test2"


def test_task_list_add_task_exception():
    test_list = TaskList()
    test_list.add_task("test")
    assert len(test_list.get_task_list()) == 0


def test_task_list_fit_task():
    test_list = TaskList()
    start_end = [1000, 2000]
    test_list.fit_task(Task(100, 0, "fit_task_1", False), start_end)
    assert test_list.get_task_list()[0].get_start_time() == 1000
    assert test_list.get_task_list()[0].get_end_time() == 1100
    test_list.add_task(Task(1130, 1200, "add_task_1", False))
    test_list.fit_task(Task(100, 0, "fit_task_2", False), start_end)
    assert test_list.get_task_list()[-1].get_start_time() == 1200
    assert test_list.get_task_list()[-1].get_end_time() == 1300
    test_list.add_task(Task(1300, 2000, "add_task_2", False))
    test_list.fit_task(Task(100, 0, "fit_task_3", False), start_end)
    assert len(test_list.get_task_list()) == 4


def test_task_list_fit_task_exception():
    test_list = TaskList()
    test_list.fit_task("test", [0, 9])
    assert len(test_list.get_task_list()) == 0


def test_remove_task():
    test_list = TaskList()
    test_1 = Task(30, 100, "test1", False)
    test_2 = Task(100, 200, "test2", False)
    test_3 = Task(100, 200, "test3", True)
    test_4 = Task(200, 230, "test4", True)
    test_list.add_task(test_1)
    test_list.add_task(test_2)
    test_list.add_task(test_3)
    test_list.add_task(test_4)
    assert len(test_list.get_task_list()) == 4
    test_list.remove_task("test2")
    assert test_list.get_task_list() == [test_1, test_3, test_4]
