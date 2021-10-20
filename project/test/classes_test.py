import pytest
from datetime import timedelta, date
from project.apis import get_weather
from project.classes import Task, TaskList, WeatherRating


def test_task():
    new_task = Task(timedelta(hours=8), timedelta(hours=9), None, None, "Swimming", False)
    assert new_task.start_time == timedelta(hours=8)
    assert new_task.end_time == timedelta(hours=9)
    assert new_task.priority() is None
    assert new_task.duration == new_task.end_time - new_task.start_time
    assert new_task.description == "Swimming"
    assert not new_task.from_g_cal


def test_task_exception():
    with pytest.raises(TypeError):
        Task(100, 200, 1, 100, True)



def test_task_list_add_task():
    test_list = TaskList()
    test_list.add_task(Task(timedelta(hours=8), timedelta(hours=9), None, None, "test", False), date.today())
    test_list.add_task(Task(timedelta(hours=10), timedelta(hours=11), None, None, "test1", False), date.today())
    test_task_list = test_list.task_list_dict
    assert len(test_task_list) == 1
    assert test_task_list[date.today()][-1].start_time == timedelta(10)
    assert test_task_list[date.today()][-1].end_time == timedelta(11)
    assert test_task_list[-1].priority is None
    assert test_task_list[date.today()][0].description == "test"
    assert test_task_list[date.today()][-1].description == "test1"
    assert not test_task_list[date.today()][-1].from_g_cal
    test_list.add_task(Task(timedelta(hours=8), timedelta(hours=9), None, None, "test2", False), date.today())
    assert test_list.task_list_dict[date.today()][-1].description == "test2"


def test_task_list_add_task_exception():
    test_list = TaskList()
    test_list.add_task("test")
    assert len(test_list.task_list_dict) == 0


def test_task_list_fit_task():
    test_list = TaskList()
    start_end = [1000, 2000]
    test_list.fit_task(Task(timedelta(0), timedelta(0), timedelta(minutes=40), 1, "test", False), start_end,
                       date.today())
    assert test_list.task_list_dict[date.today()][0].start_time == timedelta(hours=10)
    assert test_list.task_list_dict[date.today()][0].end_time == timedelta(hours=10, minutes=40)
    test_list.add_task(Task(timedelta(hours=8), timedelta(hours=9), None, None, "test2", False), date.today())
    test_list.fit_task(Task(timedelta(0), timedelta(0), timedelta(minutes=40), 1, "fit_task2", False), start_end,
                       date.today())
    assert test_list.task_list_dict[date.today()][-2].start_time == timedelta(hours=8)
    assert test_list.task_list_dict[date.today()][-2].end == timedelta(hours=9)
    test_list.add_task(Task(timedelta(hours=18), timedelta(hours=19), None, None, "test2", False), date.today())
    test_list.fit_task(Task(timedelta(0), timedelta(0), timedelta(minutes=40), 1, "fit_task3", False), start_end,
                       date.today())
    assert len(test_list.task_list_dict[date.today()]) == 4


def test_task_list_fit_task_exception():
    test_list = TaskList()
    test_list.fit_task("test", [0, 9])
    assert len(test_list.task_list_dict) == 0


def test_remove_task():
    test_list = TaskList()
    test_1 = Task(timedelta(hours=8), timedelta(hours=9), None, None, "test_1", False)
    test_2 = Task(timedelta(hours=8), timedelta(hours=9), None, None, "test_2", False)
    test_3 = Task(timedelta(hours=8), timedelta(hours=9), None, None, "test_3", False)
    test_4 = Task(timedelta(hours=8), timedelta(hours=9), None, None, "test_4", False)
    test_list.add_task(test_1, date.today())
    test_list.add_task(test_2, date.today())
    test_list.add_task(test_3, date.today())
    test_list.add_task(test_4, date.today())
    assert len(test_list.task_list_dict[date.today()]) == 4
    test_list.remove_task("test2")
    assert test_list.task_list_dict[date.today()] == [test_1, test_3, test_4]


def test_weather_rating():
    data = get_weather("Delft")
    weather_day = WeatherRating(data)
