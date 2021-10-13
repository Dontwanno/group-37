from project.weather_data import get_weather


def test_get_weather():
    # not the best test, ill admit
    assert not get_weather("Delft") == 0
    assert get_weather("soifajioadhfoiaser290358927589ewtsf") == 0
