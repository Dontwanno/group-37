from project.ui import format_int_to_time_string


def test_format_int_to_time_string():
    #assert format_int_to_time_string(0) == "0:00"
    assert format_int_to_time_string(1) == "0:01"
    assert format_int_to_time_string(30) == "0:30"
    assert format_int_to_time_string(100) == "1:00"
    assert format_int_to_time_string(1130) == "11:30"
