import requests


def get_weather(city):
    # set the api key and the url of the weather website
    api_key = "094eaa9002d7545fbda3e4c9f5956fe9"
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    # complete url
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    # get the info from the API
    response = requests.get(complete_url)
    x = response.json()
    # check if the city exists
    if x["cod"] != "404":
        print(x)
        return x
    else:
        print("City not found")


get_weather("Delft")
