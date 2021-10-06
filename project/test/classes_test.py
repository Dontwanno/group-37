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
    test_list.add_task(Task(100, 200, "test", False))
    test_task_list = test_list.get_task_list()
    assert len(test_task_list) == 1
    assert test_task_list[-1].get_start_time() == 100
    assert test_task_list[-1].get_end_time() == 200
    assert test_task_list[-1].get_description() == "test"
    assert not test_task_list[-1].get_from_g_cal()


def test_task_list_add_task_exception():
    test_list = TaskList()
    test_list.add_task("test")
    assert len(test_list.get_task_list()) == 0
